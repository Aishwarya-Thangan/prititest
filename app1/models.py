from django.db import models
from django.db.models.base import Model
from django.db.models.fields import DurationField, TimeField
from django.db.models.fields.related import ForeignKey

# Create your models here.

class common_class(models.Model):
    
    def __str__(self):
        #return f"{self.__dict__}" 
        if type(self) == Employee:
            return f"{self.id}---{self.name}"
        elif type(self) == License:
            return f"{self.license_no}----{self.expiry_date}"
        elif type(self)== Task:
            # return f"{self.task_id}----{self.name}"
            return f"{self.__dict__}"
        elif type(self) == Project:
            return f"{self.project_id}---{self.name}" 

    def __repr__(self):
        return str(self)

    class Meta:
        abstract = True    


class Employee(common_class):  # table name
    name = models.CharField(max_length=100)
    salary = models.FloatField()
    address = models.CharField(max_length=500)
    company = models.CharField(max_length=100,default = "Infosys")

    class Meta: 
        db_table = "emp"

    def get_name_with_salary(self):
        return f"Name:- {self.name} salary:- {self.salary} "

    #-------One to many relationship----
    def get_task_count(self):
        return len(self.task_set.all())

class License(common_class):
    license_no = models.CharField(primary_key=True,max_length=16)
    expiry_date = models.DateField()
    dl_type = models.CharField(max_length=10)
    employee = models.OneToOneField(Employee,on_delete = models.CASCADE)  #hare on_delete=models.CASCADE---isliye hai ki jab employee dlt ho jayega to uska license ka kuch kam nhi so o bhi dlt hona chahiye--emp+license donhi dlt honar cascade ni

    class Meta:
        db_table = "license"

#license ka object use krke uska aassociated emp fetch krna hai--
    def get_employee(self):
        return self.employee


#license se us employee ka address change krna hai--

    def change_address(self,new_adr):
        self.employee.address = new_adr
        self.employee.save()
        print("Address updated..!")


#By passing license no--we want license object-------
    #  @staticmethod
    # def get_license_obj(license_no):
    #     return License.objects.get(license_no=license_no)

 #------------------------OR (By using class method)------------------
    @classmethod
    def get_license_obj(cls,license_no):
        return cls.objects.get(license_no=license_no)

#---------------------------------------------------------------------------------------
#one to many relationship-----
#Employee has no of task--
class Task(common_class):
    task_id = models.AutoField(primary_key=True)
    name= models.CharField(max_length=100)
    timeline = models.DateField(null= True)
    task_created_date  = models.DateTimeField(auto_now_add=True) 
    employee = models.ForeignKey(Employee,null = True,on_delete=models.SET_NULL,related_name = "task")
   
    class Meta:
        db_table = "task"
   
   #Task se emp chahiye--
    def get_employee(self):
        return self.employee

#--------------------------------------------------------------------------------
#Many to many relationship-------
#one Employee has no. of projects  --and single project no. of employee can work---
class Project(common_class):
    project_id = models.AutoField(primary_key=True)
    description  = models.TextField(null= True)
    name = models.CharField(max_length=100)
    duration = models.CharField(max_length=15)
    client = models.CharField(max_length=16)
    employee =models.ManyToManyField(Employee,db_table="emp_project")
    
    
    class Meta:
        db_table = "project"

#------------------------------------------------------------------
#many-To-many----

class Common_pizza(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

    class Meta:
        abstract = True

class Topping(Common_pizza):
    pass


class pizza(Common_pizza):
    toppings = models.ManyToManyField('Topping',related_name = 'pizzas')


