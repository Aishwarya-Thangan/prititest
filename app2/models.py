
from django.db import models


# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)
    salary = models.FloatField()
    addr = models.CharField(max_length=600)
    company = models.CharField(max_length=100,default = "Infosys")

    def __str__(self):
        return f"{self.__dict__}"

    def __repr__(self):
        return str(self)

    def get_name_with_salary(self):
        return f"Name:- {self.name} salary:- {self.salary} "