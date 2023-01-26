from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField 
class User(AbstractUser):
    avatar = models.ImageField(upload_to='uploads/%Y/%m')
class Category(models.Model): 
    name = models.CharField(max_length=255,null=False, unique=True)
    def __str__(self):
        return self.name
    
class ItemBase(models.Model): 
    class Meta: 
        abstract= True

    subject = models.CharField(max_length=255, null= False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)   
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='courses/%Y/%m', default=None)
    def __str__(self):
        return self.subject

class Course(ItemBase): 
    class Meta: 
        unique_together = ('subject', 'Category')
        ordering = ['id']
    description = models.TextField(null = True, blank=True)
    Category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

class Lesson(ItemBase):
    class Meta:
        unique_together = ('subject', 'course')
    content = RichTextField()
    course = models.ForeignKey(Course , on_delete=models.SET_NULL, null = True)
    tags = models.ManyToManyField('Tag', blank=True, null=True)
    

class Tag(models.Model): 
    name = models.CharField(max_length=50, unique=True)
    def __str__(self): 
        return self.name; 





