from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.fields import BooleanField


class transactions(models.Model):

    orderID = models.CharField(
        verbose_name = ('orderID'),
        max_length=200, 
        null=True,
        help_text = ('the order id'),
    )


    billingname = models.CharField(
        verbose_name = ('Billing Name'),
        max_length=200, 
        null=True,
        help_text=('Enter your blog title here.'),
    )


    date = models.DateTimeField(
        verbose_name = ('date'),
        help_text = ('The date of the order.'),
        null=True,
    )

    total = models.FloatField(
        verbose_name = ('total'),
        null=True,
    )

    paymentstatus = models.BooleanField(
        
    )


    pay_method = (
    ('visa' , 'visa'),
    ('mastercard' , 'mastercard'),
    ('paypal' , 'paypal'),

    )
    
    

    





      



    






