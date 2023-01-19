from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    avatar = models.ImageField(upload_to='uploads/%Y/%m')
class Category(models.Model): 
    name = models.CharField(max_length=255,null=False, unique=True)
class Course(models.Model): 
    subject = models.CharField(max_length=255, null= False)
    description = models.TextField(null = True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)   
    active = models.BooleanField(default=True)
    Category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

