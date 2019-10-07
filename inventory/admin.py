from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Counterparty)
admin.site.register(ProductIncome)
admin.site.register(ProductOutcome)
admin.site.register(IncomeWarrant)
admin.site.register(OutcomeWarrant)
admin.site.register(IncomeInvoice)
admin.site.register(OutcomeInvoice)