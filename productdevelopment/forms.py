from django import forms
from django.forms import ModelForm
from productdevelopment.models import Deliverable
from .models import Worker, Production_Line, Production_Line_Worker,\
                    Production_Line_Deliverable, Finished_Bundle

class WorkerForm(ModelForm):
    worker_name = forms.CharField(max_length=500, required=True, widget=forms.
    TextInput(attrs={'class': 'form-control uk-input uk-form-width-large\
                     uk-form-success', 'placeholder': 'ex. Anakin Skywalker'}))

    worker_details = forms.CharField(max_length=500, required=True, widget=forms.
    Textarea(attrs={'class': 'form-control uk-input uk-form-width-large\
                     uk-form-success', 'placeholder': 'ex. Hates Sand'}))

    worker_number =  forms.IntegerField(required=True, widget=forms.
    NumberInput(attrs={'class': 'form-control uk-input uk-form-width-large\
                     uk-form-success uk-form-width-large uk-form-height-large',
                     'placeholder': 'ex. 09xxxxxxxxx/telephone'}))


    class Meta:
        model = Worker
        fields = '__all__'

class ProductionLineForm(ModelForm):
    line_name = forms.CharField(max_length=500, required=True, widget=forms.
    Textarea(attrs={'class': 'form-control uk-input uk-form-width-large\
                     uk-form-success', 'placeholder': 'ex. Sewing Line'}))

    line_number = forms.IntegerField(required=True, widget=forms.
    NumberInput(attrs={'class': 'form-control uk-input uk-form-width-large\
                     uk-form-success uk-form-width-large uk-form-height-large',
                     'placeholder': 'ex. 1'}))


    class Meta:
        model = Production_Line
        fields = '__all__'

class ProductionLineWorkerForm(forms.ModelForm):
    available_workers = Production_Line_Worker.objects.filter(date_removed__isnull=True).values('worker__pk')
    available = Worker.objects.exclude(pk__in=available_workers)
    worker = forms.ModelChoiceField(queryset=available, required=True, widget=forms.
        Select(attrs={'class': 'form-control uk-input uk-form-width-large\
                uk-form-success uk-form-height-large\
                uk-select',
            }))
    production_lines = Production_Line.objects.all()
    production_line = forms.ModelChoiceField(queryset=production_lines, required=True, widget=forms.
        Select(attrs={'class': 'form-control uk-input uk-form-width-large\
                uk-form-success uk-form-height-large\
                uk-select',
            }))
    class Meta:
        model = Production_Line_Worker
        fields = ('worker',
                  'production_line')

class ProductionLineDeliverableForm(ModelForm):
    class Meta:
        model = Production_Line_Deliverable
        fields = '__all__'

class FinishedBundleForm(ModelForm):
    class Meta:
        model = Finished_Bundle
        fields = '__all__'