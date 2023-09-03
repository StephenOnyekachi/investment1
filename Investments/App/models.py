from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


PENDING = "pending"
SUCCESS = "success"


STATUS = [
    (PENDING,"pending"),
    (SUCCESS,"success"),
]

    
class Users(AbstractUser):
    username = models.CharField(max_length=100, blank=True, null=True, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    number = models.TextField(default=0, null=True)
    block = models.BooleanField(default=False)
    address = models.TextField()
    gender = models.CharField(max_length=10)
    # plan = models.ForeignKey(Plans, null=True, on_delete=models.CASCADE,related_name='plan')

    plan = models.TextField(null=True)
    balance = models.FloatField(default=0.00)
    price = models.FloatField(default=0.00)
    parcent = models.FloatField(default=0.00)

    bank_name = models.TextField(null=True)
    bank_number = models.TextField(null=True)
    bank = models.TextField(null=True)
    type = models.TextField(null=True)

    def __str__(self):
        return self.username


class Plans(models.Model):
    name = models.TextField()
    price = models.FloatField(default=0.00)
    parcentage = models.IntegerField()

    def __str__(self):
        return self.name
    

class Messages(models.Model):
    name = models.TextField()
    time = models.DateTimeField(verbose_name="time", auto_now=True)
    message = models.TextField()
    picture = models.ImageField(upload_to='pics', null=True)

    def __str__(self):
        return self.name


class Histories(models.Model):
    status = models.CharField(choices=STATUS, default='pending', max_length=20)
    time = models.DateTimeField(verbose_name="time", auto_now=True)
    amount = models.TextField()

    def __str__(self):
        return self.amount
    

class AdminAccount(models.Model):
    name = models.TextField(null=True)
    number = models.TextField(null=True)
    bank = models.TextField(null=True)

    def __str__(self):
        return self.name

    
    

