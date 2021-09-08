
# from app1.models import Employee
#exec(open("C:\\Python\\B5\\Django_project\\first\\db_shell.py").read())
#-----------For connection Dbsqlite----------
# e = Employee(name = "A",salary = 58656,address = "malkapur")
# e.save()


#object --object manager
#Employee.objects.create(name = "B",salary = 894598,address = "Hyderabad")

# all_data = list(Employee.objects.all())
# print(all_data)

# all_data = Employee.objects.all()[0] #first data
# print(all_data)

# all_data =Employee.objects.all()[5]
# print(all_data.__dict__)

# all_data =list(Employee.objects.all())[-1]
# print(all_data)


# all_data = Employee.objects.all()
# print(all_data.query)

# emp = Employee.objects.filter(name="A")
# print(emp)

# all_data = Employee.objects.all()
# print(all_data)

# all_data =Employee.objects.all()[5]
# print(all_data)

#-------------------------------------------------------------------------------------
# import random
# adr_list = ["pune","Mumbai","Banglore","Hyderabad","Chennai"]
# for i in range(1,21):
#     Employee.objects.create(name = chr(65+i),salary = random.randint(35000,85000),address=random.choice(adr_list))
    
#----------------------------------------------------------------------------------

#@@@@---one to one relationship---------------------Connection with workbench-------
#--------------Employee has license --------one to one-------------is ex. of one to one relationship
#--------------Employee has multiple task----one to many
#--------------Employee
# from app1.models import Employee,License,Task  
from datetime import date
from app1.models import *


#To delete record from work bench -- here we are deleting id= 23 employee

# def delete_emp_by_id(eid):
#     emp = Employee.objects.get(id = eid)
#     emp.delete()

# delete_emp_by_id(23)

#--------------------------------------------------------------------------------
# To delete all data --
# Employee.objects.all().delete()
#-----------------------------------------------------------------------
#Jiski salary 50000 and gtr than 500000 hai uska recor dlt kro

# Employee.objects.filter(salary__gte=50000).delete()

#-----------------------------------------------------------------------------
# Actual relationship --Onetoone ----

#Creating license for employee ---eid = 22 --jiska id 22 hai uska license create kr rhe hai
# emp = Employee.objects.get(id = 22)
# print(emp)

# l=License(license_no = "MH12 57165894788",expiry_date = date(2035,12,11),dl_type = "MCWG",employee=emp)
# l.save()
#-------------------------------------------------------------------
#Creating license for employee ---eid = 21 --jiska id 21 hai uska license create kr rhe hai
# emp = Employee.objects.get(id = 21)
# print(emp)
# l=License(license_no = "MH12 6372819984",expiry_date = date(2015,11,13),dl_type = "MCWOG",employee=emp)
# l.save()


#---------OR----------above line we can as below also
# l=License(license_no = "MH12 57165894788",expiry_date = date(2035,12,11),dl_type = "MCWG",employee_id=22)
#----------OR--------------
# l = License.objects.create(license_no = "MH12 57165894788",expiry_date = date(2035,12,11),dl_type = "MCWG",employee_id=22)

# emp = Employee.objects.get(id = 22)
#print(emp)
#If we want salary--
# print(emp.salary)

#-----------------------------------------
#To get licence--
# l = License.objects.get(license_no="MH12 57165894788")
# print(l)

#-----------------------------------------
#To get license from employee---
#First we have to get employee
# emp = Employee.objects.get(id = 22)

# l1= License.objects.get(employee=emp)  #or--- l1= License.objects.get(employee=emp.id)
# print(l1)

#now same we can do by only one line--(fetch license by employee--emp_obj.secondclassname(smalletters))
# emp = Employee.objects.get(id = 22)
# print(emp.license)

#-------------------------------------------------------------
#To fetch employee by license--(ab license se employee nikalna hai..)
# l1 = License.objects.get(license_no = "MH12 57165894788").employee
# print(l1)

#--------------------------------------------------------------
# To fetch employee name from license--

# l1 = License.objects.get(license_no = "MH12 57165894788").employee.name
# print(l1)
#--------------------------------------------------------------
# To fetch employee id from license--

# l1 = License.objects.get(license_no = "MH12 57165894788").employee.id
# print(l1)


#----------------------------------------------------------------
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@---UPDATE----@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# l1 = License.objects.get(license_no = "MH12 57165894788").employee #(Here hme emp milega--o emp ka name pavan hai o hme change krna hai --Rohan krna hao ab)
# l1.name = "Rohan"
# l1.save()

#------------------------------------------------------------
#Ab hme aisa licence chahiye jiske emplyee ka name Rohan hai 
# Employee ke name se license   

# print(License.objects.get(employee__name = "Rohan"))

#-------------------------------------------------------------
# Employee ke Id se license   

# print(License.objects.get(employee__id = 22))  #Here we can write---employee=22--instead of --employee__id=22

#-------------------------------------------------------------
#-@@@@@@@@@@@@@@@@@@ Deleting license  @@@@@@@@@@@@@@@@@@@@@@@@@@@@
# l = License.objects.get(license_no = "MH12 6372819984")
#print(l)
# l.delete()

#------------------------------------------------------------------
#To dlt employee now---------
# Employee.objects.get(id = 21).delete()
#-------------------------------------------------------------
#To delete all data ---------
# Employee.objects.all().delete()

#-------------------------------------------------------------
#---By using method---get_employee ----from model file --it is an instance method so we have to create object first anf then call its method
# l = License.objects.get(license_no = "MH12 57165894788") 
# print(l.get_employee)

#--------------------------------------------------------------
#---By using method  ---change address -----from model file

# l = License.objects.get(license_no = "MH12 57165894788")   
# print(l.employee.address)   #chennai

# if hasattr(l,"change_address"):
#     l.change_address("Kolkata")
#-------------------------------------------------------------------

#--Here we are calling method---from model file------get_license_obj--static and class method also --both we are calling same ---like below----- --
# print(License.get_license_obj("MH12 57165894788"))
#---------------------------------------------------------------

#--To get object location-----------
# print(hex(id(License.get_license_obj("MH12 57165894788"))))
#-----------------------------------End one to one relationship------------------------------------------------------------


#**********Bulk creations----------

# emp_list=[Employee(name= "Rakesh1",salary = 89478.02,address = "Mumbai"),
# Employee(name = "Rakesh2",salary = 79478.02,address = "Pune"),
# Employee(name = "Rakesh3",salary = 39478.02,address = "satara"),
# Employee(name = "Rakesh4",salary = 99478.02,address = "Motala")]

# Employee.objects.bulk_create(emp_list)
#----------------------------------------------------------------------------------

#To generate randomly employee---and insert it into database using bulk----
# import random
# def generate_name():
#     name = ""
#     for i in range(0, random.randint(4,9)):
#         name += chr(64 + random.randint(1,26)) 
#     return name.title() 

# def generate_employee(num):
#     My_list = [] 
#     adr_list=["Pune","Mumbai","Thane","satara","Nashik"]
#     for i in range(1,num):
#         emp_obj =Employee(name=generate_name(),salary=random.randint(20000,50000),address=random.choice(adr_list))
#         My_list.append(emp_obj)
#     return My_list

# a = generate_employee(100)
# Employee.objects.bulk_create(a)      
# 
# --------------------------------------------------------------------------------------------------
#using id__in---
# print(Employee.objects.filter(id__in=[82,83,84]))     #Here we will get info about employee whose id = 82,83,84

#----------------------------------------------------------------------------------------------------
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2
#-------One to many relationship------------
# emp = Employee.objects.get(id = 82)
#task-1--for emp id = 82
# t1 = Task.objects.create(name= "create login page",timeline = str(date(2021,8,25)),employee=emp)  #control+g-----for jumping perticular line no
# print(t1)
#------------------------------------
#task-2--
# Task.objects.create(name = "create email functionality")
#-------------------
#task-3---
# Task.objects.create(name = "create homepage")

#------------------------------------------------------
#function --to assigning task to employee---
#here jo third no ka task hai table me workbench ke --vh task emp_id = 83 ko assign krna hai
# def assign_task_to_emp(emp_id,timeline,task_id):
#     emp = Employee.objects.get(id = emp_id)
#     task_obj = Task.objects.get(task_id = task_id)
#     task_obj.employee = emp
#     task_obj.timeline = timeline
#     task_obj.save()
# assign_task_to_emp(83,date(2021,8,20),3)

#-----------------------------------------------------
#ab ek perticular employee ke sare task nikalna hai to----here we take employee_id=83
#83 no ke employee ke sare task nikalo---
# emp = Employee.objects.get(id = 83)
# print(emp.task_set.all())   #----emp.class ka name small_letters _set.all()
#-----------------------------------------------------
#Employee se task---
#Ab 83 no ke employee ka first task nikalna hai to-----------

# emp = Employee.objects.get(id = 83)
# print(emp.task_set.all()[0])   #----emp.class ka name small_letters _set.all()
#-------------------------------------------------
#check --emp_id=83 ---ke pas-- total kitne task hai
# emp = Employee.objects.get(id = 83)
# print(len(emp.task_set.all()))  #

#---------------------------------------------------
#task se employee---
#ab hme task se employee nikalna hai
#ye task_id = 3 ye task konse employee ko assign kiya hai?

# t = Task.objects.get(task_id = 3).employee
# print(t)
#-------------------------------------------------------
# employee se sare task ke count--
#Employee me method likhi hai--get_task_count--models file me--so we all calling this method here
#first afall create object of emp bcz this method is instance with self so we want object for calling it
#Hrere emp 83 ke pure kitne task hai o check kr rhe hai..

# emp = Employee.objects.get(id = 83)
# print(emp.get_task_count())

#--------------------------------------------------------------
#calling this instance method get_employee --written in Task class----in models.py--
#Here task 3 konse emp ke pas hai o check kr rhe hai...

# t = Task.objects.get(task_id = 3)
# print(t.get_employee())
#--------------------------------------------------------------
#Here we will not use in print--task.set.all--we will use only--emp.task.all--
# bcz we write in task class--related name = task
#Here also we will get emp=83 ke pass konse konse  task hai

# emp = Employee.objects.get(id = 83)
# print(emp.task.all())

#---------------------------------------------------------------------#
#********Note---jab task me related name = task likhoge to-- task.set_all vala nhin kam krega

####################################################################################
#Pizza and topping --many to many

#create first pizza-----and---- first Topping-----
# # hawaiian_pizza = pizza.objects.create(name = 'Hawaiian')  #create pizza name
# pineapple = Topping(name = 'pineapple') #create topping name
# pineapple.save()

#-----------------------------------------------------
#create second pizza-----and---- second  Topping-----

# cheese_pizza = pizza.objects.create(name = 'cheese')  #create pizza name
# apple = Topping(name = 'apple') #create topping name
# apple.save()

# #------------------------------------------------------------
###############Now adding Toppings on pizza----


#@@@@@@@@@------pizza se toppings-----
#Here we are aadding pineapple topping on chawaiian_pizza --
# hawaiian_pizza = pizza.objects.create(name = 'Hawaiian')  
# pineapple = Topping(name = 'pineapple') 

# hawaiian_pizza.toppings.add(pineapple)

#------------------------------------------------------------
#Here we are aadding pineapple topping on cheese pizza--
# cheese_pizza = pizza.objects.create(name = 'cheese')
# pineapple = Topping(name = 'pineapple') 

# cheese_pizza.toppings.add(pineapple)

# #----------------------------------
# hawaiian_pizza = pizza.objects.create(name = 'Hawaiian')  
# apple = Topping(name = 'apple') 
# apple.save()
# hawaiian_pizza.toppings.add(apple)
# #-------------------------------------
# hawaiian_pizza = pizza.objects.create(name = 'Hawaiian')  
# pineapple = Topping(name = 'pineapple') 
# pineapple.save()
# hawaiian_pizza.toppings.add(pineapple)

#---------------------------------------------
# hawaiian_pizza = pizza.objects.create(name = 'Hawaiian')  
# apple = Topping(name = 'apple')
# apple.save()
# hawaiian_pizza.toppings.add(apple)
#-----------------------------------------------
#To check id=12 pizaa ke pas konsi toppings hai
# Pizza = pizza.objects.get(id =12) 
# print(Pizza.toppings.all())
#---------------------------------------------
#To add new topping on id=12 pizza
# Pizza = pizza.objects.get(id =12) 
# t1 = Topping(name = "capsicum")
# t1.save()
# Pizza.toppings.add(t1)
#-----------------------------

# Pizza = pizza.objects.get(id =7) 
# t1 = Topping.objects.get(id = 15)
# Pizza.toppings.add(t1)
# #--------------------------------------
# pizza1 = pizza.objects.create(name = "cheese1")
# t1 = Topping.objects.get(id = 8)
# t2 = Topping.objects.get(id = 9)
# pizza1.toppings.add(t1)
# pizza1.toppings.add(t2)
#-----------------------------------------------------------------
#@@@@@@@@@@@@@@-------------Toppings se pizza-------------
#abhi phle jis topping ke pizaa nikalna hai o ---topping get kro--I want 15 no topping ke pizaa

# t1 = Topping.objects.get(id = 15)
# print(t1.pizza_set.all()) #t1.pizza class small letter me.all()

#------------------------------------------------------------
#Ab Pizza class me model.py file me change kiya --ie ralated name = pizzas so---abhi pizaa_set.all() nhi chlega--
#we will get same ans like above statement--

# t1 = Topping.objects.get(id = 15)  #We are checking i=15 ke pass konse konse pizza hai..!
# print(t1.pizzas.all()) #t1.pizza class smal letter me.all()

#--------------------------------------------------------------
#Eise pizza chahiye jiske topping ka name start hoga 'p' se--

# print(pizza.objects.filter(toppings__name__startswith ='p'))
#-------------------------------------------------------------









