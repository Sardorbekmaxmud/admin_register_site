from django.db import models


# Create your models here.
class Faculty(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'faculties'


class Kafedra(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    first_name = models.CharField(max_length=80, null=True, blank=True)
    last_name = models.CharField(max_length=80, null=True, blank=True)
    age = models.PositiveSmallIntegerField()
    subject = models.ForeignKey(Subject, null=True, on_delete=models.CASCADE)
    kafedra = models.ForeignKey(Kafedra, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Group(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.ForeignKey(Faculty, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    group = models.ForeignKey(Group, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='images', null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
