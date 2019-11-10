from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.


class ProductCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'


class Counterparty(models.Model):
    name = models.CharField(max_length=200)
    saldo = models.DecimalField(max_digits=20, decimal_places=2, default=0)

    class Meta:
        verbose_name = 'Контрагент'
        verbose_name_plural = 'Контрагенты'


class Product(models.Model):
    name = models.CharField(max_length=200)
    measure_unit = models.CharField(max_length=5)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    in_stock = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    category = models.ForeignKey(
        ProductCategory, on_delete=models.SET_NULL,
        blank=True, null=True, related_name='products')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


# add reference to user who created documents

class IncomeWarrant(models.Model):
    name = models.CharField(max_length=20)
    issued_date = models.DateField(default=timezone.now)
    received_from = models.ForeignKey(
        Counterparty, on_delete=models.PROTECT, related_name='cash_incomes')
    cash_amount = models.DecimalField(
        max_digits=20, decimal_places=2, default=0)
    comment = models.CharField(max_length=100)
    registered = models.BooleanField(default=False)

    _original_state = None

    def __init__(self, *args, **kwargs):
        super(IncomeWarrant, self).__init__(*args, **kwargs)
        self._original_state = self.registered

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        if self.registered != self._original_state:
            if self.registered:
                self.received_from.saldo -= self.cash_amount
            else:
                self.received_from.saldo += self.cash_amount
            self.received_from.save(force_update=True)

        super(IncomeWarrant, self).save(
            force_insert, force_update, *args, **kwargs)
        self.__original_state = self.registered

    def validate_registration(self):
        if self.name != '' and self.cash_amount != 0.0:
            return True
        else:
            return False

    class Meta:
        verbose_name = 'Приходный кассовый ордер'
        verbose_name_plural = 'Приходные кассовые ордера'


class OutcomeWarrant(models.Model):
    name = models.CharField(max_length=20)
    issued_date = models.DateField(default=timezone.now)
    given_to = models.ForeignKey(
        Counterparty, on_delete=models.PROTECT, related_name='cash_outcomes')
    cash_amount = models.DecimalField(
        max_digits=20, decimal_places=2, default=0)
    comment = models.CharField(max_length=100)
    registered = models.BooleanField(default=False)

    __original_state = None

    def __init__(self, *args, **kwargs):
        super(OutcomeWarrant, self).__init__(*args, **kwargs)
        self.__original_state = self.registered

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        if self.registered != self.__original_state:
            if self.registered:
                self.given_to.saldo += self.cash_amount
            else:
                self.given_to.saldo -= self.cash_amount
            self.given_to.save(force_update=True)

        super(OutcomeWarrant, self).save(
            force_insert, force_update, *args, **kwargs)
        self.__original_state = self.registered

    def validate_registration(self):
        if self.name != '' and self.cash_amount != 0.0:
            return True
        else:
            return False

    class Meta:
        verbose_name = 'Расходный кассовый ордер'
        verbose_name_plural = 'Расходные кассовые ордера'


class IncomeInvoice(models.Model):
    name = models.CharField(max_length=20)
    issued_date = models.DateField(default=timezone.now)
    received_from = models.ForeignKey(
        Counterparty, on_delete=models.PROTECT, related_name='invoices_income')
    total = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    registered = models.BooleanField(default=False)

    __original_state = None

    def __init__(self, *args, **kwargs):
        super(IncomeInvoice, self).__init__(*args, **kwargs)
        self.__original_state = self.registered

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        if self.registered != self.__original_state:
            if self.registered:
                self.received_from.saldo -= self.total
                for item in self.items.all():
                    item.product.in_stock += item.quantity
                    item.product.save(force_update=True)
            else:
                self.received_from.saldo += self.total
                for item in self.items.all():
                    item.product.in_stock -= item.quantity
                    item.product.save(force_update=True)
            self.received_from.save(force_update=True)

        super(IncomeInvoice, self).save(
            force_insert, force_update, *args, **kwargs)
        self.__original_state = self.registered

    def validate_registration(self):
        if self.name != '' and self.cash_amount != 0.0:
            if self.items.all():
                valid_items = True
                for item in self.items.all():
                    if item.price == 0 or item.quantity == 0:
                        valid_items = False
                return valid_items
        return False

    class Meta:
        verbose_name = 'Приходная накладная'
        verbose_name_plural = 'Приходные накладные'


class OutcomeInvoice(models.Model):
    name = models.CharField(max_length=20)
    issued_date = models.DateField(default=timezone.now)
    given_to = models.ForeignKey(
        Counterparty, on_delete=models.PROTECT,
        related_name='invoices_outcome')
    total = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    registered = models.BooleanField(default=False)

    __original_state = None

    def __init__(self, *args, **kwargs):
        super(OutcomeInvoice, self).__init__(*args, **kwargs)
        self.__original_state = self.registered

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        if self.registered != self.__original_state:
            if self.registered:
                self.given_to.saldo += self.total
                for item in self.items.all():
                    item.product.in_stock -= item.quantity
                    item.product.save(force_update=True)
            else:
                self.given_to.saldo -= self.total
                for item in self.items.all():
                    item.product.in_stock += item.quantity
                    item.product.save(force_update=True)
            self.given_to.save(force_update=True)

        super(OutcomeInvoice, self).save(
            force_insert, force_update, *args, **kwargs)
        self.__original_state = self.registered

    def validate_registration(self):
        if self.name != '' and self.cash_amount != 0.0:
            if self.items.all():
                valid_items = True
                for item in self.items.all():
                    if item.price == 0 or item.quantity == 0:
                        valid_items = False
                return valid_items
        return False

    class Meta:
        verbose_name = 'Расходная накладная'
        verbose_name_plural = 'Расходные накладные'


class ProductIncome(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name='income')
    price = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    invoice = models.ForeignKey(
        IncomeInvoice, on_delete=models.CASCADE, related_name='items')
    quantity = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=20, decimal_places=2, default=0)

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        self.total = self.price * self.quantity
        super(ProductIncome, self).save(
            force_insert, force_update, *args, **kwargs)

    class Meta:
        verbose_name = 'Приход товара'
        verbose_name_plural = 'Приходы товара'


@receiver(post_save, sender=ProductIncome)
def product_income_post_save(sender, **kwargs):
    product_income_instance = kwargs.get('instance')
    invoice = IncomeInvoice.objects.get(pk=product_income_instance.invoice.id)
    invoice.total = 0
    for item in invoice.items.all():
        invoice.total += item.total
    invoice.save(force_update=True)


class ProductOutcome(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name='outcome')
    price = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    invoice = models.ForeignKey(
        OutcomeInvoice, on_delete=models.CASCADE, related_name='items')
    quantity = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=20, decimal_places=2, default=0)

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        self.total = self.price * self.quantity
        super(ProductOutcome, self).save(
            force_insert, force_update, *args, **kwargs)

    class Meta:
        verbose_name = 'Расход товара'
        verbose_name_plural = 'Расходы товара'


@receiver(post_save, sender=ProductOutcome)
def product_outcome_post_save(sender, **kwargs):
    product_outcome_instance = kwargs.get('instance')
    invoice = OutcomeInvoice.objects.get(
        pk=product_outcome_instance.invoice.id)
    invoice.total = 0
    for item in invoice.items.all():
        invoice.total += item.total
    invoice.save(force_update=True)
