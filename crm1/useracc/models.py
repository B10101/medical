from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name


class Customer(models.Model):
    user = models.ForeignKey(User, max_length=200, null=True, on_delete= models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    child = models.CharField(max_length=200, null=True, default="None")
    email = models.EmailField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)

    def save(self):
        super().save()

    def __str__(self):
        return self.name


class Vaccine(models.Model):
    customer = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=1000, null=True)
    date_for_administration = models.DateTimeField(null=True)
    status = models.CharField(max_length=200, null=True)




class Reservation(models.Model):
    STATUS = (
        ('pending', 'Pending'),
        ('checked', 'Checked')
    )
    DOCTOR = (
        ('dentist','Dentist'),
        ("children's doctor","Children's doctor")
    )
    customer = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    doctor = models.CharField(max_length=200, null=True,choices=DOCTOR)
    Id_number = models.IntegerField(null=True)
    date_reserved = models.DateTimeField(null=True)
    status = models.CharField(max_length=200, null=True,choices=STATUS, default='Pending')
