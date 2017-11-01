from django.db import models


class Supplier(models.Model):
    supplier_name = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    contact_number = models.IntegerField()
    email = models.EmailField(max_length=100)

    def __str__(self):
        return  self.supplier_name + " " + str(self.pk)

class Part(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=19, decimal_places=10)
    description = models.CharField(max_length=200)
    color = models.CharField(max_length=100)
    measurements = models.CharField(max_length=500)
    order_specifications = models.CharField(max_length=100)
    stock = models.DecimalField(max_digits=19, decimal_places=10)#quantity
    PART_TYPE_CHOICE = (
        ('fabric','fabric'),
        ('accessory','accessory'),
    )
    part_type = models.CharField(max_length=100, choices=PART_TYPE_CHOICE)

    def __str__(self):
        return  self.name + " " + str(self.pk)

class Purchase_Order(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    date_sent = models.DateField()
    terms_of_payment = models.CharField(max_length=100)
    prepared_by = models.CharField(max_length=100)
    approved_by = models.CharField(max_length=100)
    po_number = models.CharField(max_length=100)

    def __str__(self):
        return  self.po_number

class Purchase_Order_Item(models.Model):
    purchase_order = models.ForeignKey(Purchase_Order, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    quantity = models.IntegerField()
    color = models.CharField(max_length=100)
    uom = models.CharField(max_length=20)
    date_due = models.DateField()
    unit_price = models.IntegerField()

    def __str__(self):
        return  self.description + " " + str(self.pk)

class Part_In(models.Model):
  part = models.ForeignKey(Part, on_delete=models.CASCADE)
  quantity = models.DecimalField(max_digits=19, decimal_places=10)
  date = models.DateField()#auto add

class Part_Out(models.Model):
  part = models.ForeignKey(Part, on_delete=models.CASCADE)
  deliverable = models.ForeignKey('productdevelopment.Deliverable', on_delete=None)
  quantity = models.DecimalField(max_digits=19, decimal_places=10)
  date = models.DateField()