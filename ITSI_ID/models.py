from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=55, name="name")
    surname = models.CharField(max_length=55, name="surname") 
    
    password = models.CharField(max_length=55, name="password")
    
    avatar = models.ImageField(name="avatar", upload_to="avatar", null=True, blank=True)
    
    team = models.ManyToManyField("Users", verbose_name="team", name="team", blank=True)
    
    products = models.ManyToManyField("Products", verbose_name="products", name="products", blank=True)
    
    services = models.ManyToManyField("Services", verbose_name="services", name="services", blank=True)
    
    analytics = models.ManyToManyField("API", verbose_name="analytics", name="analytics", blank=True)
 
class API(models.Model):
    January = models.IntegerField(default=0)
    February = models.IntegerField(default=0)
    March = models.IntegerField(default=0)
    April = models.IntegerField(default=0)
    May = models.IntegerField(default=0)
    June = models.IntegerField(default=0)
    July = models.IntegerField(default=0)
    August = models.IntegerField(default=0)
    September = models.IntegerField(default=0)
    October = models.IntegerField(default=0)
    November = models.IntegerField(default=0)
    December = models.IntegerField(default=0)
    
class Products(models.Model):
    name = models.CharField(max_length=55, name="name")
    
class Services(models.Model):
    name = models.CharField(max_length=55, name="name")