from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.


class Books(models.Model):
    name = models.CharField(max_length=100)
    Author = models.CharField(max_length=70)
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    

    def __str__(self):
        return f"{self.id} {self.name}  {self.Author} {self.description} {self.price}"


class MyUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    password01 = models.CharField(max_length=128)
    password02 = models.CharField(max_length=128)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    cart = models.ManyToManyField(Books, blank=True, related_name="cart")
    

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'



