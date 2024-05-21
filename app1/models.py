from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    
    confirmation = models.CharField(max_length=50)
    roleChoice = (
        ('Owner','Owner'),
        ('Client','Client')
    )
    role = models.CharField(max_length=50,choices=roleChoice)

class House(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    beds = models.PositiveIntegerField()
    baths = models.PositiveIntegerField()
    image = models.ImageField(upload_to='images/', blank=True)
    description = models.TextField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated','-created']

    def __str__(self):
        return self.name

class Reservation(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    house = models.ForeignKey(House,on_delete=models.CASCADE)
    startDate = models.DateField()
    endDate = models.DateField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated','-created']

    
    def __str__(self):
        return self.house.name
