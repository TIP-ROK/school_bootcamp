from django.db import models
from school_app.models import School


class Department(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=45)
    duration = models.DateField()
    is_active = models.BooleanField()
    description = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    M = 'Male'
    F = 'Female'
    GENDER = [
        (M, 'Male'),
        (F, 'Female')
    ]
    gender = models.CharField(max_length=6, choices=GENDER)
    salary = models.DecimalField(max_digits=9, decimal_places=2)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name

    def save(self, *args, **kwargs):
        for field_name in ['first_name', 'last_name']:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.capitalize())
        super(Employee, self).save(*args, **kwargs)
