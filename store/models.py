from email.policy import default
from turtle import title
from django.db import models

class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()

class Collection(models.Model):
    item = models.CharField(max_length=255)
    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name= '+')

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collections = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotions = models.OneToOneField(Promotion, on_delete=models.PROTECT)

class Customer(models.Model):
#Here we are definig the vvalue seperatly incase we want to change the default 
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'
#Thois is a fixed list of values 
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold'),
    ]
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=225)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices= MEMBERSHIP_CHOICES, default= MEMBERSHIP_BRONZE)

class Order(models.Model):
    PAYMENT_PENDING = 'P'
    PAYMENT_COMPLETE = 'C'
    PAYMENT_FAILED ='F'
    PAYMENT_STATUS_CHOICES= [
        (PAYMENT_PENDING, 'Pending'),
        (PAYMENT_COMPLETE, 'Complete'),
        (PAYMENT_FAILED, 'Failed'),
    ]
    placed_at= models.DateTimeField(auto_now_add= True)
    payment_status= models.CharField(
        max_length=1, choices=PAYMENT_STATUS_CHOICES, default= PAYMENT_PENDING
    )
    customer= models.ForeignKey(Customer, on_delete=models.PROTECT)

class OrderItem(models.Model):
        order = models.ForeignKey(Order, on_delete=models.PROTECT)
        product = models.ForeignKey(Product, on_delete=models.PROTECT)
        quantity= models.PositiveSmallIntegerField()
        unit_price= models.DecimalField(max_digits=6, decimal_places=2)

class Address(models.Model):
        street = models.CharField(max_length=255)
        city = models.CharField(max_length=255)
        customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)


class Cart(models.Model):
    created_at= models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()