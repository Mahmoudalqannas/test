from django.db import models
import datetime
from datetime import timedelta

SUB_CHOICES = [
    (360,'One Year 400$'),
    (180, 'Six months 250$'),
    (90, 'Three months 150$')
]
class Customers(models.Model):

    first_name = models.CharField(max_length = 25 )
    last_name = models.CharField(max_length = 25)
    customer_phone = models.IntegerField()
    customer_helth = models.BooleanField()

    def __str__(self):
        return self.first_name  

class Subscription(models.Model):
    customer_sub = models.ForeignKey(to = 'Customers' , on_delete = models.PROTECT)
    start_date = models.DateTimeField()
    period = models.IntegerField(choices=SUB_CHOICES)
    payment = models.IntegerField()

    # def __str__(self):
    #     return self.customer_sub.first_name
    
  

    @property
    def sub_end_date(self):

        return self.start_date + timedelta(days=self.period)

class VisitCustomer(models.Model):
    customer_visit = models.ForeignKey(to = 'Subscription' , on_delete = models.PROTECT )
    visit_date = models.DateTimeField(default = datetime.datetime.now() )


    # def end_of_sub():
    #     pass

# Create your models here.
