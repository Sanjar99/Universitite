from django.contrib import admin

from .models import Student,Faculty,Groups

admin.site.register(Faculty)
admin.site.register(Groups)
admin.site.register(Student)


# Register your models here.
