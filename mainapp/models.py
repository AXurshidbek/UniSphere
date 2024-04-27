from django.db import models
from userapp.models import User

class Region(models.Model):
    name=models.CharField(max_length=25)

class Center(models.Model):
    name=models.CharField(max_length=55)
    description=models.TextField()
    profile_pic=models.FileField()
    admin=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    phone_num1=models.CharField(max_length=15)
    phone_num2=models.CharField(max_length=15, null=True, blank=True)
    phone_num3=models.CharField(max_length=15, null=True, blank=True)
    adress=models.TextField()
    map_location=models.CharField(max_length=500)
    website=models.CharField(max_length=55)
    region=models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.name

class Pictures(models.Model):
    file=models.FileField()
    object=models.ForeignKey(Center, on_delete=models.CASCADE)


class Category(models.Model):
    name=models.CharField(max_length=105)
    
class Course(models.Model):
    name=models.CharField(max_length=255)
    description = models.TextField()
    profile_pic=models.FileField()
    category=models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    center=models.ForeignKey(Center, on_delete=models.CASCADE)


    def __str__(self):
        return self.name



class Vacancy(models.Model):
    name=models.CharField(max_length=205)
    description=models.TextField()
    center=models.ForeignKey(Center, on_delete=models.CASCADE)
    course=models.ForeignKey(Course, on_delete=models.CASCADE)


    def __str__(self):
        return self.name


