from django.db import models
from productdevelopment.models import Order, Deliverable, Operations, Bundle

class Worker(models.Model):
    worker_name = models.CharField(max_length=500)
    worker_details = models.CharField(max_length=500)
    worker_number = models.IntegerField()

    def __str__(self):
        return  self.worker_name + " " + str(self.pk)

class Production_Line(models.Model):
    line_name = models.CharField(max_length=500)
    line_number = models.IntegerField()

    def __str__(self):
        return  self.line_name + "pk:" + str(self.pk)

class Production_Line_Worker(models.Model):
    worker = models.ForeignKey(Worker, on_delete=None)
    production_line = models.ForeignKey(Production_Line, on_delete=None)
    date_added = models.DateTimeField(auto_now_add=True)
    date_removed = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return  self.production_line.line_name + " " + str(self.worker.worker_name)

class Production_Line_Deliverable(models.Model):#assign deliverable to production_line
    production_line = models.ForeignKey(Production_Line, on_delete=None)
    deliverable = models.ForeignKey(Deliverable, on_delete=None)
    operations = models.ManyToManyField(Operations, blank=True)

class Finished_Bundle(models.Model):
    bundle = models.ForeignKey(Bundle, on_delete=None)
    production_line_worker = models.ForeignKey(Worker, on_delete=None)
    date_finished = models.DateTimeField()
    operation = models.ForeignKey(Operations, on_delete=None)
