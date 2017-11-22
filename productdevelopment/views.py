from django.shortcuts import render, redirect
from .forms import CustomerForm, OrderForm, DeliverableForm, \
                     OperationsForm
from .models import Customer, Order, Deliverable, \
                    Operations
# from materialplanning.models import Part
import time
from datetime import date, datetime
import math
from decimal import *

"""def add_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            form = CustomerForm()
            first_name = request.user.first_name
            last_name = request.user.last_name
            args = {'added': 'true', 'form': form}
            return render(request, 'productdevelopment/add_customer.html', args)

        else:
            args = {'invalid_data': 'true', 'form': form}
            return render(request, 'productdevelopment/add_customer.html', args)

    else:
        form = CustomerForm()
        args = {'form': form}
        return render(request, 'productdevelopment/add_customer.html', args)

def add_order(request):
    if request.method == "POST":
        args = {}
        orderForm = OrderForm(request.POST)
        print(request.POST)
        if orderForm.is_valid():
            order = orderForm.save()
            order = Order.objects.filter(pk=order.pk)
            args.update({'order': 'true'})


            for count in range(len(request.POST.getlist('start_date'))):
                start_date = request.POST.getlist('start_date')[count]
                start_date = datetime.strptime(start_date, "%Y-%m-%d")
                end_date = request.POST.getlist('end_date')[count]
                end_date = datetime.strptime(end_date, "%Y-%m-%d")


                deliverableFormData = { 'order' : order,
                                        'start_date' : start_date,
                                        'end_date' : end_date,
                                        'size' : request.POST.getlist('size')[count],
                                        'quantity' : int(request.POST.getlist('quantity')[count]),
                }

                deliverable = DeliverableForm(deliverableFormData)
                print(deliverable.errors)

                if deliverable.is_valid():
                    deliverable = deliverable.save()
                    surplus = deliverable.quantity%50;
                    bundles = math.floor(deliverable.quantity/50)
                    deliverable = Deliverable.objects.filter(pk=deliverable.pk)
                    args.update({'deliverable': 'true'})
                    print("DELIVERABLE SSAVED")


                    print("surplus:"+str(surplus)+" quantity:"+str(bundles))

                    number=1 
                    while number <= bundles:
                        bundleFormData = { 'deliverable': deliverable,
                                           'quantity': 50,

                        }

                        bundle = BundleForm(bundleFormData)
                        print(bundle)

                        if bundle.is_valid():
                            bundle.save()
                            print("bundle saved")

                        number+=1

                    if surplus > 0:
                        bundleFormData = { 'deliverable': deliverable,
                                           'quantity': surplus,
                        }

                        bundle = BundleForm(bundleFormData)
                        print(bundleFormData)

                        if bundle.is_valid():
                            bundle.save()
                            args.update({'bundle': 'true'})
                            print("surplus bundle saved")





            costingFormData = { 'order' : order,
                                'labor_cost' : Decimal(request.POST.getlist('labor_cost')[0]),
                                'overhead_cost' : Decimal(request.POST.getlist('overhead_cost')[0]),
            }
            costing = CostingForm(costingFormData)

            print(costing.errors)
            if costing.is_valid():
                args.update({'costing': 'true'})
                costing = costing.save()
                costing = Costing.objects.filter(pk=costing.pk)
                print("COSTING SAVE")
                parts = Part.objects.all();


                for count in range(len(request.POST.getlist('part'))):
                    costingPartsFormData = { 'costing' : costing,
                                             'consumption' : request.POST.getlist('consumption')[count],
                                             'part' : Part.objects.filter(pk=int(request.POST.getlist('part')[count])),
                    }
                    costingPart = CostingPartsForm(costingPartsFormData)
                    print(costingPart.errors)
                    if costingPart.is_valid():
                        costingPart.save()
                        print("COSTING PART SAVE")


            for count in range(len(request.POST.getlist('number'))):
                operationsFormData = { 'order' : order,
                                       'number' : request.POST.getlist('number')[count],
                                       'operation' : request.POST.getlist('operation')[count],
                                       'material' : request.POST.getlist('material')[count],
                                       'stitch' : request.POST.getlist('stitch')[count],
                                       'description' : request.POST.getlist('description')[count],
                                       'minutes' : request.POST.getlist('minutes')[count],
                                       'machine' : request.POST.getlist('Machine')[count],

                }
                operation = OperationsForm(operationsFormData)
                if operation.is_valid:
                    args.update({'operations': 'true'})
                    operation.save()
                    print("operation saved")
                    args.update({'added': 'true'})
        form = OrderForm()
        args.update({'form': form})
        return render(request, 'productdevelopment/add_order.html', args)

    else:
        form = OrderForm()
        parts = Part.objects.all()
        args = {'form': form, 'parts': parts}
        return render(request, 'productdevelopment/add_order.html', args)"""