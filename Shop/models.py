from django.db import models
from django.contrib.auth.models import User

# Create your models here.
DIVISION_CHOICES = (
    ('Dhaka','Dhaka'),
    ('Rangpur','Rangpur'),
    ('Rajshahi','Rajshahi'),
    ('khulna','khulna'),
    ('chttogram','chttogram'),
)


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=34)
    division = models.CharField(choices=DIVISION_CHOICES, max_length=59)
    district = models.CharField(max_length=200)
    thana = models.CharField(max_length=60)
    villorroad = models.CharField(max_length=200)
    zipCode = models.IntegerField()

    def __str__(self):
        return str(self.id)
    

CATEGORY_CHOICES = (
    ('L','Lehenga'),
    ('S','Saree'),
    ('GP','Gents Pant'),
    ('BK','Borkha'),
    ('BF','baby Fishion'),
)


class Product(models.Model):
    title = models.CharField(max_length=300)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=40)
    category = models.CharField(choices=CATEGORY_CHOICES , max_length=3)
    product_image = models.ImageField(upload_to='productImg')
    
    def __str__(self):
        return str(self.id)
    


class Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
    

STATUS_CHOICE = (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On the Way','On the Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
)


class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    quantity = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS_CHOICE, max_length=30, default='Panding')