from django.db import models

class Staff(models.Model):
    ROLE_CHOICES = (
        ('professor', 'Professor'),
        ('assistant', 'Assistant'),
        ('admin', 'Administrator'),
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    department = models.CharField(max_length=100)
    def __str__(self):
        return self.first_name + self.last_name