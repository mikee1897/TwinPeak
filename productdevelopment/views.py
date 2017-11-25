from django.shortcuts import render, redirect
from .forms import *
from .models import *

"""helpes save landline/mobile/email to a customer object instance"""
def add_a_customer_contact_person_helper_function(request, ccpf):
    customer = Customer_Contact_Person.objects.filter(ccpf.pk)
    for count in range(
        len(request.POST.getlist(
            ccpf.contact_name + 'landline'))):
        clnf = CustomerLandlineNumberForm({
            'customer': request.POST.get(customer),
            'landline_number': request.POST.getlist(
                ccpf.contact_name + 'landline')[count],
        })
        clnf.save()

    for count in range(
        len(request.POST.getlist(
            ccpf.contact_name + 'mobile'))):
        cmnf = CustomerMobileNumberForm({
            'customer': request.POST.get(customer),
            'mobile_number': request.POST.getlist(
                ccpf.contact_name + 'mobile')[count],
        })
        cmnf.save()

    for count in range(
        len(request.POST.getlist(
            ccpf.contact_name + 'email'))):
        cef = CustomerEmailForm({
            'customer': request.POST.get(customer),
            'email': request.POST.getlist(
                ccpf.contact_name + 'email')[count],
        })
        cef.save()

def add_a_customer(request):
    if request.method == 'POST':
        cf = CustomerForm(request.POST)
        if cf.is_valid():
            cf = cf.save() # save the customer

            """for each customer, save their contact persons"""
            for count in range(len(request.POST.getlist('contact_name'))):
                contactPersonName = request.POST.getlist('contact_name')[count]
                contactPersonDepartment = request.POST.getlist('department')[count]
                ccpf = CustomerContactPersonForm({
                    'customer': Customer.objects.filter(pk=cf.pk),
                    'contact_name': contactPersonName,
                    'department': contactPersonDepartment,
                })

                """each contact person will get all their landline/mobile/email
                will be saved"""
                if ccpf.is_valid():
                    ccpf = ccpf.save()

                    add_a_customer_contact_person_helper_function(request, ccpf)
                    
        args = {'successfully_added': 'True'}
        return render(request, 'productdevelopment/add_a_customer.html', args)
    else:
        return render(request, 'productdevelopment/add_a_customer.html')


def add_new_style(request):
    if request.method == 'POST':
        return render(request, 'productdevelopment/add_new_style.html')
    else:
        return render(request, 'productdevelopment/add_new_style.html')
