from django.db import models

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.name

class Groups(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    group = models.ForeignKey(Groups, on_delete=models.CASCADE)
    enrollment_year = models.IntegerField()
    def __str__(self):
        return self.first_name + self.last_name