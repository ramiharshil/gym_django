from birthday.fields import BirthdayField
from django.db import models
from django import forms
import birthday
# Create your models here.
#
# GENDER_CHOICES = (
#    ('M', 'Male'),
#    ('F', 'Female')
# )
# feesp_choices = (('P', 'Paid'),
#                  ('NP', 'NotPaid'))
#
# tranningtype_choices = (('B', 'Basic'),
#                  ('PT', 'PersonalTranning'),('PPT', 'PatnerPersonalTranning'),('GT', 'GroupTranning'))

class clientdetails(models.Model):
    name = models.CharField(max_length=50)
    age = models.DurationField(default=None)
    gender = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    mobileno = models.CharField(max_length=10)
    address = models.CharField(max_length=150)
    diseases = models.CharField(max_length=200)
    packagep = models.CharField(max_length=50)
    packages = models.DateTimeField()
    packagee = models.DateTimeField()
    feesp = models.CharField(max_length=50)
    tranningtype = models.CharField(max_length=20)
    dob = models.DateField()

    def __str__(self):
        return f"{self.name} {self.dob}"

