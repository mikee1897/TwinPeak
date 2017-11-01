from django.db import models
from materialplanning.models import Part


class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    contact_number = models.IntegerField()
    email = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return  self.customer_name

#customer has diff orders, but orders only have one customer -many to one relationship
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    program_name = models.CharField(max_length=100)
    collection = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    style_number = models.CharField(max_length=100)
    description = models.CharField(max_length=500)


    def __str__(self):
        return  self.program_name + " " + str(self.pk)

class Deliverable(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    DELIVERABLE_TYPE_CHOICE = (
        ('32A,','32A,'),
        ('32B','32B'),
        ('34A','34A'),
        ('34B','34B'),
        ('36A','36A'),
        ('36B','36B'),
    )
    size = models.CharField(max_length=5,choices=DELIVERABLE_TYPE_CHOICE)
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.pk)

class Operations(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    number = models.IntegerField()
    operation = models.CharField(max_length=500)
    material = models.CharField(max_length=500)
    stitch = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    minutes = models.CharField(max_length=500)
    machine = models.CharField(max_length=500)

    def __str__(self):
        return  str(self.pk) + " " + str(self.operation)

"""automatically created in views.py"""
class Bundle(models.Model):
    deliverable = models.ForeignKey(Deliverable)
    quantity = models.DecimalField(max_digits=19, decimal_places=10)
    finished =  models.NullBooleanField(blank=True)

    def __str__(self):
        return  str(self.deliverable.pk) + " " + str(self.quantity)

class Costing(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    labor_cost = models.DecimalField(max_digits=19, decimal_places=10)
    overhead_cost = models.DecimalField(max_digits=19, decimal_places=10)

    def __str__(self):
        return str(self.pk)

class Costing_Parts(models.Model):
    costing = models.ForeignKey(Costing, on_delete=models.CASCADE)
    consumption = models.CharField(max_length=500)
    part = models.ForeignKey(Part, on_delete=models.CASCADE)

    def __str__(self):
        return  self.part.name + " " + str(self.pk)
