# Generated by Django 2.2.3 on 2019-07-31 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Counterparty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('saldo', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
            options={
                'verbose_name': 'Контрагент',
                'verbose_name_plural': 'Контрагенты',
            },
        ),
        migrations.CreateModel(
            name='IncomeInvoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('issued_date', models.DateField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=20)),
                ('registered', models.BooleanField(default=False)),
                ('received_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoices_income', to='inventory.Counterparty')),
            ],
            options={
                'verbose_name': 'Приходная накладная',
                'verbose_name_plural': 'Приходные накладные',
            },
        ),
        migrations.CreateModel(
            name='OutcomeInvoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('issued_date', models.DateField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=20)),
                ('registered', models.BooleanField(default=False)),
                ('gicen_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoices_outcome', to='inventory.Counterparty')),
            ],
            options={
                'verbose_name': 'Расходная накладная',
                'verbose_name_plural': 'Расходные накладные',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('measure_unit', models.CharField(max_length=5)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('in_stock', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'Категория товара',
                'verbose_name_plural': 'Категории товаров',
            },
        ),
        migrations.CreateModel(
            name='ProductOutcome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=20)),
                ('total', models.DecimalField(decimal_places=2, max_digits=20)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='inventory.OutcomeInvoice')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products_outcome', to='inventory.Product')),
            ],
            options={
                'verbose_name': 'Расход товара',
                'verbose_name_plural': 'Расходы товара',
            },
        ),
        migrations.CreateModel(
            name='ProductIncome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=20)),
                ('total', models.DecimalField(decimal_places=2, max_digits=20)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='inventory.IncomeInvoice')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products_income', to='inventory.Product')),
            ],
            options={
                'verbose_name': 'Приход товара',
                'verbose_name_plural': 'Приходы товара',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.ProductCategory'),
        ),
        migrations.CreateModel(
            name='OutcomeWarrant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('issued_date', models.DateField()),
                ('cash_amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('comment', models.CharField(max_length=100)),
                ('registered', models.BooleanField(default=False)),
                ('received_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cash_outcome', to='inventory.Counterparty')),
            ],
            options={
                'verbose_name': 'Расходный кассовый ордер',
                'verbose_name_plural': 'Расходные кассовые ордера',
            },
        ),
        migrations.CreateModel(
            name='IncomeWarrant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('issued_date', models.DateField()),
                ('cash_amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('comment', models.CharField(max_length=100)),
                ('registered', models.BooleanField(default=False)),
                ('received_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cash_income', to='inventory.Counterparty')),
            ],
            options={
                'verbose_name': 'Приходный кассовый ордер',
                'verbose_name_plural': 'Приходные кассовые ордера',
            },
        ),
    ]