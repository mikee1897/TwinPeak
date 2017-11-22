
from django import forms
from django.forms import ModelForm
from .models import Customer, Order, Deliverable,\
                    Operations

class CustomerForm(ModelForm):
    customer_name = forms.CharField(max_length=100, required=True)

    contact_name = forms.CharField(max_length=100, required=True)

    contact_number = forms.IntegerField(required=True)
    email = forms.CharField()
    description = forms.CharField(max_length=500, required=True)

    class Meta:
        model = Customer
        fields = '__all__'


class OrderForm(ModelForm):
    customers = Customer.objects.all()
    customer = forms.ModelChoiceField(queryset=customers, required=True)

    program_name = forms.CharField(max_length=100, required=True,)

    collection = forms.CharField(max_length=100, required=True)

    brand = forms.CharField(max_length=100, required=True)

    style_number = forms.CharField(max_length=100, required=True)

    description = forms.CharField(max_length=500, required=True)
    class Meta:
        model = Order
        fields = '__all__'

class DeliverableForm(ModelForm):
    class Meta:
        model = Deliverable
        fields = '__all__'

class OperationsForm(ModelForm):
    class Meta:
        model = Operations
        fields = '__all__'