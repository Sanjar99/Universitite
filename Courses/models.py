from django.db import models
from Staffs.models import Staff
from Students.models import Student

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    credits = models.IntegerField()
    semester = models.IntegerField()
    teacher = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, limit_choices_to={'role': 'professor'})
    def __str__(self):
        return self.name

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enroll_date = models.DateField(auto_now_add=True)
    grade = models.FloatField(null=True, blank=True)
