from gymapp.models import Subscription, VisitCustomer, Customers
from django import forms
from django.forms.models import ModelForm

class CustomersForm(ModelForm):
    class Meta:
        model = Customers
        exclude = []

class SubscriptionForm(ModelForm):
    class Meta:
        model = Subscription
        exclude = []
    
class VisitCustomerForm(ModelForm):
    class Meta:
        model = VisitCustomer
        exclude = []

        