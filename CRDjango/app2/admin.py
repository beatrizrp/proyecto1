from django.contrib import admin

from app2.models import *

class SchoolAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']
    search_fields = ['name']
    list_filter = ['address']

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'age']
    search_fields = ['name']
    list_filter = ['age']


admin.site.register(School, SchoolAdmin)
admin.site.register(Student, StudentAdmin)