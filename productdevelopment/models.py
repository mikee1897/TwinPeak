from django.db import models


class Customer(models.Model):
    customer_name = models.CharField(max_length=500)


class Customer_Contact_Person(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    contact_name = models.CharField(max_length=500)
    department = models.CharField(max_length=100)


class Customer_Landline_Number(models.Model):
    customer = models.ForeignKey(
        Customer_Contact_Person, on_delete=models.CASCADE)
    landline_number = models.CharField(max_length=50)


class Customer_Mobile_Number(models.Model):
    customer = models.ForeignKey(
        Customer_Contact_Person, on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=50)


class Customer_Email (models.Model):
    customer = models.ForeignKey(
        Customer_Contact_Person, on_delete=models.CASCADE)
    email = models.CharField(max_length=500)

# not sure if this is needed; if kept, make optional

"""
class Customer_Brand(models.Model):
    customer = models.ForeignKey(Customer)
    brand_name = models.CharField(max_length=500)


class Customer_Collection(models.Model):
    customer = models.ForeignKey(Customer)
    # delete if class Customer_Brand is deleted
    brand = models.ForeignKey(Customer_Brand)
    year = models.IntegerField()
    season = models.CharField(max_length=500)
"""


class Style(models.Model):
    # customer = models.ForeignKey(Customer)
    # brand = models.ForeignKey(Customer_Brand)
    # collection = models.ForeignKey(Customer_Collection)
    style_name = models.CharField(max_length=500)
    style_id = models.CharField(max_length=500)
    collection_name = models.CharField(max_length=500)
    year = models.DateField()


class Style_Size(models.Model):
    style = models.ForeignKey(Style, on_delete=models.CASCADE)
    size = models.CharField(max_length=10)


class Size_Specifications(models.Model):
    size = models.ForeignKey(Style_Size, on_delete=models.CASCADE)


class Material_Cost(models.Model):
    style_size = models.ForeignKey(Style_Size, on_delete=models.CASCADE)
    # import material details from Material Planning


class Labor_Cost(models.Model):
    style = models.ForeignKey(Style, on_delete=models.CASCADE)
    cutting_cost = models.DecimalField(max_digits=19, decimal_places=10)
    sewing_cost = models.DecimalField(max_digits=19, decimal_places=10)
    washing_cost = models.DecimalField(max_digits=19, decimal_places=10)
    finishing_cost = models.DecimalField(max_digits=19, decimal_places=10)
    examining_cost = models.DecimalField(max_digits=19, decimal_places=10)
    pressing_cost = models.DecimalField(max_digits=19, decimal_places=10)
    packaging_cost = models.DecimalField(max_digits=19, decimal_places=10)
    final_inspection_cost = models.DecimalField(
        max_digits=19, decimal_places=10)


class Overhead_Cost(models.Model):
    style = models.ForeignKey(Style, on_delete=models.CASCADE)
    rent_cost = models.DecimalField(max_digits=19, decimal_places=10)
    utility_cost = models.DecimalField(max_digits=19, decimal_places=10)
    paper_cost = models.DecimalField(max_digits=19, decimal_places=10)
    machine_maintenance_cost = models.DecimalField(
        max_digits=19, decimal_places=10)
    transportation_gas_cost = models.DecimalField(
        max_digits=19, decimal_places=10)
    transportation_maintenance_cost = models.DecimalField(
        max_digits=19, decimal_places=10)
    communication_cost = models.DecimalField(max_digits=19, decimal_places=10)


class Operations(models.Model):
    style = models.ForeignKey(Style, on_delete=models.CASCADE)
    number = models.IntegerField()
    operation_name = models.CharField(max_length=500)
    # foreign key on class Material_Cost
    material = models.CharField(max_length=500)
    stitch = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    minutes = models.IntegerField()
    machine = models.CharField(max_length=500)


class Order(models.Model):
    style = models.ForeignKey(Style, on_delete=models.CASCADE)
    purchase_order_number = models.IntegerField()
    # image field - optional
    delivery_address = models.TextField()

# change class name of Deliverable class to more appropriate term


class Deliverable(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    start_delivery_date = models.DateTimeField()
    end_delivery_date = models.DateTimeField()
    DELIVERABLE_TYPE_CHOICE = (
        ('32A', '32A'),
        ('32B', '32B'),
        ('34A', '34A'),
        ('34B', '34B'),
        ('36A', '36A'),
        ('36B', '36B'),
    )
    size = models.CharField(max_length=5, choices=DELIVERABLE_TYPE_CHOICE)
    quantity = models.IntegerField()
