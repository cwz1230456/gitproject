from django.db import models
from django.contrib.auth.models import User
class Salary(models.Model):
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    total = models.CharField(max_length=100)
    remarks = models.CharField(max_length=100)

class Month(models.Model):
    nameID = models.ForeignKey(Salary)
    month = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)

class Invoice(models.Model):
    title = models.CharField(max_length=100)
    drawer = models.CharField(max_length=100)
    date = models.CharField(max_length=100)

class InDetail(models.Model):
    productionID = models.ForeignKey(Invoice)
    production = models.CharField(max_length=100)
    number = models.IntegerField(max_length=100)
    Univalent = models.CharField(max_length=100)
    total = models.CharField(max_length=100)   
    
class People(models.Model):
    user = models.ForeignKey(User)

class Tax(models.Model):
    costing = models.FloatField(max_length=100)
    selling = models.FloatField(max_length=100)
    addvalue = models.FloatField(max_length=100)
    nation = models.FloatField(max_length=100)
    
class Form(models.Model):
    year = models.CharField(max_length=100)
    
class FormDetail(models.Model):
    yearincomeID = models.ForeignKey(Form)
    yearincome = models.CharField(max_length=100)
    yearcost = models.CharField(max_length=100)
    sellingexpenses = models.CharField(max_length=100)
    managementexpenses = models.CharField(max_length=100) 
    financialexpenses = models.CharField(max_length=100)
    incomefrominvestment  = models.CharField(max_length=100)