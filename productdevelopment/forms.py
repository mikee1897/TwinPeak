
from django import forms
from django.forms import ModelForm
from .models import Customer, Order, Deliverable, Costing, Costing_Parts,\
                    Operations, Bundle

class CustomerForm(ModelForm):
    customer_name = forms.CharField(max_length=100, required=True, widget=forms.
    TextInput(attrs={'class': 'form-control uk-input uk-form-width-large\
                     uk-form-success', 'placeholder': 'ex. The First Order'}))

    contact_name = forms.CharField(max_length=100, required=True, widget=forms.
    TextInput(attrs={'class': 'form-control uk-input uk-form-width-large\
                     uk-form-success', 'placeholder': 'ex. Kylo Ren'}))

    contact_number = forms.IntegerField(required=True, widget=forms.
    NumberInput(attrs={'class': 'form-control uk-input uk-form-width-large\
                     uk-form-success uk-form-width-large uk-form-height-large',
                     'placeholder': 'ex. 09xxxxxxxxx/telephone'}))
    email = forms.CharField(widget=forms.
    EmailInput(attrs={'class': 'form-control uk-input uk-form-width-large\
                     uk-form-success uk-form-width-large uk-form-height-large',
                     'placeholder': 'ex. Publicity@Lucasfilm.com'}))

    description = forms.CharField(max_length=500, required=True, widget=forms.
    Textarea(attrs={'class': 'form-control uk-form-width-large uk-text-area\
                     uk-form-success ',
                     'rows': '3',
                     'placeholder': 'ex. Political and Military Faction, Likes Evil Looking Clothes'}))

    class Meta:
        model = Customer
        fields = '__all__'

class BundleForm(ModelForm):
    class Meta:
        model = Bundle
        fields = '__all__'


class OrderForm(ModelForm):
    customers = Customer.objects.all()
    customer = forms.ModelChoiceField(queryset=customers, required=True, widget=forms.
    Select(attrs={'class': 'form-control uk-input uk-form-width-large\
                     uk-form-success'}))

    program_name = forms.CharField(max_length=100, required=True, widget=forms.
    TextInput(attrs={'class': 'form-control uk-input uk-form-width-large\
                     uk-form-success', 'placeholder': 'ex. Put Something Here'}))

    collection = forms.CharField(max_length=100, required=True, widget=forms.
    TextInput(attrs={'class': 'form-control uk-input uk-form-width-large\
                     uk-form-success',  'placeholder': 'ex. Put Something Here'}))

    brand = forms.CharField(max_length=100, required=True, widget=forms.
    TextInput(attrs={'class': 'form-control uk-input uk-form-width-large\
                     uk-form-success',  'placeholder': 'ex. Put Something Here'}))

    style_number = forms.CharField(max_length=100, required=True, widget=forms.
    TextInput(attrs={'class': 'form-control uk-input uk-form-width-large\
                     uk-form-success',  'placeholder': 'ex. Put Something Here'}))

    description = forms.CharField(max_length=500, required=True, widget=forms.
    Textarea(attrs={'class': 'form-control uk-form-width-large uk-text-area\
                     uk-form-success ',
                     'rows': '3',
                     'placeholder': 'ex. Put Whatever Description You Feel Like Putting Here'}))
    class Meta:
        model = Order
        fields = '__all__'


class DeliverableForm(ModelForm):
    class Meta:
        model = Deliverable
        fields = '__all__'

#the specific item
class CostingForm(ModelForm):
    class Meta:
        model = Costing
        fields = '__all__'

class CostingPartsForm(ModelForm):
    class Meta:
        model = Costing_Parts
        fields = '__all__'

class OperationsForm(ModelForm):
    class Meta:
        model = Operations
        fields = '__all__'