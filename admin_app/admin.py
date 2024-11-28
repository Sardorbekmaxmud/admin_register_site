from django.contrib import admin
from .models import Faculty, Kafedra, Subject, Teacher, Group, Student

# Register your models here.
admin.site.register(Faculty)
admin.site.register(Kafedra)
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Group)
admin.site.register(Student)
