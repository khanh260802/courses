from django.contrib import admin
from .models import Category, Course, Lesson, Tag
from django.utils.html import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
# Register your models here.

class LessonForm(forms.ModelForm): 
    content = forms.CharField(widget=CKEditorUploadingWidget)
    class Meta: 
        modals = Lesson 
        fields = '__all__'

class LessonAdmin(admin.ModelAdmin): 
    class Media: 
        css = {
            'all': ('/static/css/main.css',)
        }
    form = LessonForm
    list_display = ['id', 'subject', 'create_date', 'active', 'course']
    search_fields = ['subject', 'course__subject']
    list_filter = ['subject', 'course__subject']
    readonly_fields = ['avatar']
    def avatar(self, lesson): 
        return mark_safe('''
            <img src = '/static/{img_url}' width = 120px>   
        '''.format(img_url = lesson.image.name))
    

admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Tag)













