# from django.db import models
from django.db.models import query,QuerySet
# from django.db.models.aggregates import count,Sum

from app2.models import Person
#exec(open("C:\\Python\\B5\\Django_project\\first\\db_shell2.py").read())

#-----for connection with DBslite3
#way - 2(To insert data in table)
# p1 = Person(name = "pqr",salary = 457647.01,address = "abcd") 
# p1.save()

#way - 3(To insert data in table)
#Person.objects.create(name = "sita",salary = 6389.01,address ="pune")

#To fetch data --

#To fetch all_data
# all_data = Person.objects.all()
# print(all_data)

#To fetch single_data
# all_data = Person.objects.first()
# print(all_data)

#To fetch dictionar of first_data
# all_data = Person.objects.first().__dict__
# print(all_data)

# all_data = list(Person.objects.all()) #here we will get list
# print(all_data)

# all_data = Person.objects.all()[0] #here we will get first data
# print(all_data)

# all_data = Person.objects.all()[5] #here we will get sixth data
# print(all_data)


# all_data = list(Person.objects.all())[-1] #here we will get list
# print(all_data)

#to get query
# all_data = Person.objects.all()
# print(all_data.query)

#To fetch single data by passing its id
# p1= Person.objects.get(id = 4)
# print(p1)

# p1= Person.objects.filter(id = 4)  #by filter we can get multiple data also
# print(p1)

#To get query
# p1= Person.objects.filter(id = 4)
# print(p1.query)

# p1= Person.objects.filter(name = "priti")
# print(p1)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#-----for connection with workbench--
# p1 = Person(name = "pqr",salary = 457647.01,address = "abcd") 
# p1.save()

# #for adding multiple data in workbench of table first_db
# import random
# adr_list = ["pune","Mumbai","Banglore","Hyderabad","Chennai"]
# for i in range(1,21):
#     Person.objects.create(name = chr(65+i),salary = random.randint(35000,85000),address=random.choice(adr_list))
    
#####################################################################################
#Fetching data from workbench

#To fetch all data--
# p1= Person.objects.all()  #query set return kreg
# print(p1)


#To print data in list
# p1= list(Person.objects.all())
# print(p1)

#To get record bt id
# p1= Person.objects.get(id=5)
# print(p1)


#To get filtered data
# p1= Person.objects.filter(name = "pqr")
# print(p1)

#To get single data or multiple by filter   #----filter se queryset milega..
# p1= Person.objects.filter(name = "A")   #Queryset reurn krega
# print(p1)                            

#To check length of A--it will give how many record presnts of A
# p1= Person.objects.filter(name = "A")   
# print(len(p1))                            

#------OR--------
# p1= Person.objects.filter(name = "A").count()  
# print(p1)                           

# p1= Person.objects.filter(name = "A",salary = 56778) 
# print(p1)                           

# p1= Person.objects.all().exclude(name="A")
# print(p1)


#To get single single data

# for i in Person.objects.all():
#     print(i)

# for i in Person.objects.all():
# #     print(i.name)
# format1 = """
# ---------- ID:- {} -----------
# Name:- {}
# Salary:- {}
# Address:- {}
# """
# for i in Person.objects.all():
#     print(format1.format(i.id,i.name,i.salary,i.address))

#----------------------------

# def get_person_dict():
#     per_list = []
#     for i in Person.objects.all():
#         per_list.append({"ID":i.id, "Name":i.name, "salary":i.salary, "Address":i.address})
#     return person_list

# print(get_per_dict())

#p1 = Person.objects.first()
#print(p1)
#print(dir(p1))
#print(hasattr(p1,"get_name_with_salary"))


# total_payout = 0
# for i in Person.objects.all():
#     total_payout += i.salary

# from functools import reduce

# l = reduce(lambda x, y: x["salary"]+y["salary"],[{'salary':58565.0},{'salary': 58565.0}])
# print(l)
# l = [{'salary':40.0},{'salary':656.0},{'salary':780.0}]

# t = reduce(lambda x,y:x+y,list(map(lambda x:x["salary"],l)))
# print(t)
#-----------------

#To calculate avg salary
#from django.db.models import Avg,Max

# p1 = Person.objects.all().aggregate(Avg("salary"))
#print(p1)

#----------------------------------------------

#To calculate max salary
# p1 = Person.objects.all().aggregate(Max("salary"))
# print(p1)
#--------------------------------------------
#Here we write method in model file and calling this method here ...in that we are passing id 
# and by passing id we got here person name and his salary

# p1 = Person.objects.get(id = 3)
# print(p1.get_name_with_salary)

#########################################################################################
#----------To update data(workbench)-------------

# To incerement salary of all person by 5%

# def increment_sal(increment_val):
#     all_persons = Person.objects.all()
#     for i in all_persons:
#         i.salary = i.salary + (i.salary*(increment_val/100))
#         i.save()

# increment_sal(5)

#---------------------------------------------------

#update by using id--
# hare id=4 record jo workbench ke table me present hai uska name hm change kr rhe ie=BBB
# But here id=4 hm ..id se fetch kr rhe hai..function me id pass kr ke


# Here we are updating name of person whoes id=4..and its name = B--present in our workbench table
# Now we are giving name to its person = BBB

# def update_person(p1_id,first_name):
#     p1_obj = Person.objects.get(id = p1_id)  #id = p_id
#     # print(p1_obj)
#     p1_obj.name = first_name
#     #print(p1_obj.name)
#     p1_obj.save()
#     print("Person objects updeted successfully..!")

# update_person(4,"BBB")

#--------------------------------------------------
# update by using name----
# Here jiska name "A" hai usko updete krke uska name hm BBB kr rhe hai..
# Here hm update by using name kar rhe hai..means in function we are passing name of person
#  which we wants to update..

#But hmare table me --A nam ke multiple records hai so error will raise ..and here we are \
# handling that errors..ie.--multiple objects return..!

# def update_person(name,first_name):
#     try:
#        p1_obj = Person.objects.get(name = name) 
#     except Person.DoesNotExist:
#         print(f"Person with id {name} does not exist..!") 
#     except Person.MultipleObjectsReturned:
#         print(f"More than single record return by query..!")
#     else:
#         p1_obj.name = first_name
#         p1_obj.save()
#         print("Person objects updeted successfully..!")

# update_person("A","BBB")

#-------------------------------------------------------------
# To change company name from --infosys to --TCS (update company name)
# Person.objects.all().update(company="TCS")
# Person.objects.all().filter(name ="A").update(company="cybage")

#print(hasattr(Person.objects.all(),"update"))

#-----------------------------------------------------------
# jiski id 5 se greater hei uska record hme chahiye--
# p1 = Person.objects.filter(id__gt=5)
# print(p1)

#------------------------------------------------
# jiski id 5 hai aur greater than 5  hei uska record hme chahiye--

# p1 = Person.objects.filter(id__gte=5)
# print(p1)

#-----------------------------------------------

#jiski id 5 hai aur less than 5 hei uska record hme chahiye--

# p1 = Person.objects.filter(id__lte=5)
# print(p1)

#----------------------------------------------------------------

#jiski id less than 5 hei uska record hme chahiye--

# p1 = Person.objects.filter(id__lt=5)  #in taht all operations mension above double underscore is necessory--single underscore nhi chlega
# print(p1)

#-----------------------------------------------------------------
# jiska nam N se start hai uska record chahiye--

# print(Person.objects.filter(name__startswith= "N")) 
#-----------------------------------------------------------------
# jiska nam N se start hai uska record chahiye--
#But here isstart me jo i hai uska meaning case insensetive hai means "n" and "N" ke bhi record hme milenge

# print(Person.objects.filter(name__istartswith= "N")) 
#---------------------------------------------------------------

#jiska nam "ha" se end nuva  hai uska record chahiye--

# print(Person.objects.filter(name__endswith= "ha"))
#-----------------------------------------------------------
#jiska nam "ha" and "HA" se end nuva  hai uska record chahiye--so here iendswith krna pdega--i means case insensitive--

# print(Person.objects.filter(name__iendswith= "ha"))
#-----------------------------------------------------------
#jiska nam end huva hai ha and HA se uska record---
# To check query--
# a = Person.objects.filter(name__endswith= "ha")
# print(a.query)

########################################################################################
#@@@@@@@@@@@@@@@@@@@@@@ Deleting record   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# To delete record from work bench -- here we are deleting id= 23 person

# def delete_person_by_id(eid):
#     p1 = Person.objects.get(id = eid)
#     p1.delete()

# delete_person_by_id(23)

#--------------------------------------------------------------------------
#To dlt all data---

# Person.objects.all().delete()
#--------------------------------------------------------------------------


