from django.contrib import admin
from unfold.admin import ModelAdmin 

from .models import Student 

@admin.register(Student)
class StudentAdmin(ModelAdmin):
    list_display = ['name']


