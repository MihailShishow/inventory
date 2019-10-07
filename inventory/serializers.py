from .models import Product, ProductCategory, Counterparty, IncomeWarrant, OutcomeWarrant, IncomeInvoice, OutcomeInvoice, ProductIncome, ProductOutcome
from rest_framework import serializers

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['in_stock',]



class CounterpartySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Counterparty
        fields = '__all__'
        read_only_fields = ['saldo',]


class IncomeWarrantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IncomeWarrant
        fields = '__all__'


class OutcomeWarrantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OutcomeWarrant
        fields = '__all__'


class ProductCategorySerializer(serializers.HyperlinkedModelSerializer):

    products = ProductSerializer(many=True, read_only=True)


    class Meta:
        model = ProductCategory
        fields = '__all__'


class ProductIncomeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ProductIncome
        fields = '__all__'
        read_only_fields = ['total',]


class ProductOutcomeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ProductOutcome
        fields = '__all__'
        read_only_fields = ['total',]



class IncomeInvoiceSerializer(serializers.HyperlinkedModelSerializer):
    
    items = ProductIncomeSerializer(many=True, read_only=True)

    class Meta:
        model = IncomeInvoice
        fields = '__all__'
        read_only_fields = ['total',]


class OutcomeInvoiceSerializer(serializers.HyperlinkedModelSerializer):

    items = ProductOutcomeSerializer(many=True, read_only=True)
    

    class Meta:
        model = OutcomeInvoice
        fields = '__all__'
        read_only_fields = ['total',]


# PRODUCT CIRCULATION REPORT SERIAlIZERS


class CounterpartyReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counterparty
        fields = '__all__'
        read_only_fields = ['__all__']



class IncomeInvoiceReportSerializer(serializers.ModelSerializer):
    
    received_from = CounterpartyReportSerializer(read_only=True)

    class Meta:
        model = IncomeInvoice
        fields = '__all__'
        read_only_fields = ['__all__']


class OutcomeInvoiceReportSerializer(serializers.ModelSerializer):
    
    received_from = CounterpartyReportSerializer(read_only=True)

    class Meta:
        model = OutcomeInvoice
        fields = '__all__'
        read_only_fields = ['__all__']


class ProductFilteredListSerializer(serializers.ListSerializer):

    def to_representation(self, data):
        data = data.filter(invoice__registered=True, invoice__issued_date__range=(self.context['start_date'], self.context['end_date']))
        return super().to_representation(data)


class ProductIncomeReportSerializer(serializers.ModelSerializer):

    invoice = IncomeInvoiceReportSerializer(read_only=True)

    class Meta:
        model = ProductIncome
        fields = '__all__'
        read_only_fields = ['__all__']
        list_serializer_class = ProductFilteredListSerializer


class ProductOutcomeReportSerializer(serializers.ModelSerializer):

    invoice = OutcomeInvoiceReportSerializer(read_only=True)

    class Meta:
        model = ProductOutcome
        fields = '__all__'
        read_only_fields = ['__all__']
        list_serializer_class = ProductFilteredListSerializer


class ProductReportSerializer(serializers.ModelSerializer):
    income = ProductIncomeReportSerializer(read_only=True, many=True)
    outcome = ProductOutcomeReportSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['__all__']


# COUNTERPARTY CIRCULATION BY DATE RANGE REPORT SERIALIZERS


class DocumentFilteredListSerializer(serializers.ListSerializer):

    def to_representation(self, data):
        data = data.filter(registered=True, issued_date__range=(self.context['start_date'], self.context['end_date']))
        return super().to_representation(data)



class IncomeWarrantReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = IncomeWarrant
        fields = ['name', 'issued_date', 'cash_amount', 'comment', 'registered']
        read_only_fields = ['__all__']
        list_serializer_class = DocumentFilteredListSerializer


class OutcomeWarrantReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = OutcomeWarrant
        fields = ['name', 'issued_date', 'cash_amount', 'comment', 'registered']
        read_only_fields = ['__all__']
        list_serializer_class = DocumentFilteredListSerializer


class IncomeInvoiceReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = IncomeInvoice
        fields = ['name', 'issued_date', 'total', 'registered']
        read_only_fields = ['__all__']
        list_serializer_class = DocumentFilteredListSerializer


class OutcomeInvoiceReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = OutcomeInvoice
        fields = ['name', 'issued_date', 'total', 'registered']
        read_only_fields = ['__all__']
        list_serializer_class = DocumentFilteredListSerializer



class CounterpartyReportSerializer(serializers.ModelSerializer):

    cash_incomes = IncomeWarrantReportSerializer(many=True, read_only=True)
    cash_outcomes = OutcomeWarrantReportSerializer(many=True, read_only=True)
    invoices_income = IncomeInvoiceReportSerializer(many=True, read_only=True)
    invoices_outcome = OutcomeInvoiceReportSerializer(many=True, read_only=True)
    

    class Meta:
        model = Counterparty
        fields = '__all__'
        read_only_fields = ['__all__']



