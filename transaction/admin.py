from django.contrib import admin
from .models import transactions

@admin.register(transactions)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('orderID', 'billingname', 'date', 'total', 'paymentstatus')
    list_filter = ('orderID', 'billingname', 'date', 'total', 'paymentstatus')