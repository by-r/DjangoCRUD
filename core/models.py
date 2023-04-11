from django.db import models

# Create your models here.
""" name, companyname, ICnumber, date """


class Person(models.Model):

    name = models.CharField(max_length=50)
    companyname = models.CharField(max_length=100)
    ic = models.CharField(max_length=15)
    date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name
