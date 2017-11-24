
from django import forms
from django.forms import ModelForm
from .models import *


class CustomerForm(ModelForm):

    class Meta:
        model = Customer
        fields = '__all__'


class CustomerContactPersonForm(ModelForm):

    class Meta:
        model = Customer_Contact_Person
        fields = '__all__'


class CustomerLandlineNumberForm(ModelForm):

    class Meta:
        model = Customer_Landline_Number
        fields = '__all__'


class CustomerMobileNumberForm(ModelForm):

    class Meta:
        model = Customer_Mobile_Number
        fields = '__all__'


class CustomerEmailForm(ModelForm):

    class Meta:
        model = Customer_Email
        fields = '__all__'
