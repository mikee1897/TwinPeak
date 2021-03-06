from django.shortcuts import render, redirect
from .forms import *
from .models import *
import re

"""helpes save landline/mobile/email to a customer object instance"""
def add_a_customer_contact_person_helper_function(
    request,
    ccpf,
    count_
):
    errors = False
    customer = Customer_Contact_Person.objects.filter(pk=ccpf.pk)
    for count in range(
        len(request.POST.getlist(
            'landline_number' + str(count_)))):
        clnf = CustomerLandlineNumberForm({
            'customer': customer,
            'landline_number': request.POST.getlist(
                'landline_number' + str(count_))[count],
        })
        if clnf.is_valid():
            clnf.save()
        else:
            errors = True

    for count in range(
        len(request.POST.getlist(
            'contact_number' + str(count_)))):
        cmnf = CustomerMobileNumberForm({
            'customer': customer,
            'mobile_number': request.POST.getlist(
                'contact_number' + str(count_))[count],
        })
        if cmnf.is_valid():
            cmnf.save()
        else:
            errors = True

    for count in range(
        len(request.POST.getlist(
            'email' + str(count_)))):
        cef = CustomerEmailForm({
            'customer': customer,
            'email': request.POST.getlist(
                'email' + str(count_))[count],
        })
        if cef.is_valid():
            cef.save()
        else:
            errors = True

    return errors

def add_a_customer(request):
    if request.method == 'POST':
        errors = False
        args = {}
        customerFormPK = 0
        cf = CustomerForm(request.POST)
        if cf.is_valid():
            cf = cf.save()
            # returns the keys matching the regex, ex ['contact_name1', 'contact_name2']
            contactPersons = [person for person in request.POST if re.match(r'^contact_name[0-9]*', person)]
            count = 0
            for count in range(len(contactPersons)):
                count += 1
                contactPersonName = request.POST.getlist('contact_name' + str(count))
                contactPersonDepartment = request.POST.getlist('department' + str(count))
                ccpf = CustomerContactPersonForm({
                    'customer': Customer.objects.filter(pk=cf.pk),
                    'contact_name': contactPersonName,
                    'department': contactPersonDepartment,
                })
                if ccpf.is_valid():
                    ccpf = ccpf.save()
                    # returns a boolean value
                    errors = add_a_customer_contact_person_helper_function(
                        request,
                        ccpf,
                        count)
        else:
            # cf is not valid, no instance of customer is saved, cascades on other models
            errors = True
        if errors == True:
            # TODO: do some error stuff
            pass
        return redirect('/add_new_style/'+ str(cf.pk))
    else:
        return render(request, 'productdevelopment/add_a_customer.html')


def add_new_style(request, pk=None):
    if pk and request.method == 'POST':
        print(pk)
        return render(request, 'productdevelopment/add_new_style.html')
    else:
        return render(request, 'productdevelopment/add_new_style.html')

def add_new_style_customer(request):
    pass
