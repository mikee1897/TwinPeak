from django.db import models

class Supplier(models.Model):
	supplier_name = models.CharField(max_length=100)

class Supplier_Contact_Person(models.Model):
	supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
	contact_name = models.CharField(max_length=100)
	department = models.CharField(max_length=100)

class Supplier_Landline_Number(models.Model):
	supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
	landline_number = models.IntegerField()

class Supplier_Mobile_Number(models.Model):
	supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
	mobile_number = models.IntegerField()

class Supplier_Email (models.Model):
	supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
	email = models.CharField(max_length=100)

class Raw_Material(models.Model):
	supplier = models.ForeignKey(Supplier)
	raw_material_name = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=19, decimal_places=10)
    quantity = models.DecimalField(max_digits=19, decimal_places=10)

class Raw_Material_Entry(models.Model):
	raw_material = models.ForeignKey(Raw_Material)
	quantity = models.DecimalField(max_digits=19, decimal_places=10)
	date_updated = models.DateTimeField()
	#need a field showing details of user that made the update

class Raw_Material_Exit(models.Model):
	raw_material = models.ForeignKey(Raw_Material)
	quantity = models.DecimalField(max_digits=19, decimal_places=10)
	date_updated = models.DateTimeField()
	#need a field showing details of user that made the update
