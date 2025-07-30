from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import os
# Create your models here.

def get_file_path(request, filename):
    original_filename= filename
    filename = "%s" % (original_filename)
    return os.path.join('uploads/', filename)


class catagory(models.Model):
    slug = models.CharField(max_length=150, null=False, blank=False)
    name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to = get_file_path, null=True, blank=True)
    short_description = models.CharField(max_length=150, null=True, blank=False)
    discount_upto = models.FloatField(null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class product(models.Model):
    Catagory = models.ForeignKey(catagory, null=True, on_delete=models.CASCADE)
    slug = models.CharField(max_length=150, null=True, blank=False)
    name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to = get_file_path, null=True, blank=True)
    first_side_image = models.ImageField(upload_to = get_file_path, null=True, blank=True)
    second_side_image = models.ImageField(upload_to = get_file_path, null=True, blank=True)
    third_side_image = models.ImageField(upload_to = get_file_path, null=True, blank=True)
    fourth_side_image = models.ImageField(upload_to = get_file_path, null=True, blank=True)
    short_description = models.TextField(max_length=600, null=True, blank=False)
    description = models.TextField(max_length=1000, null=False, blank=False)
    quantity = models.IntegerField(null=True, blank=False)
    reating = models.FloatField(null=False, blank=False)
    original_price= models.FloatField(null=False, blank=False)
    selling_price= models.FloatField(null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0=default, 1=hidden")
    trending = models.BooleanField(default=False, help_text="0=default, 1=trending")
    tag=models.CharField(max_length=150, null=True, blank=False)
    offer = models.CharField(max_length=150, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    product_qty = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=False)
    email = models.CharField(max_length=150, null=False)
    phone = models.CharField(max_length=150, null=False)
    city = models.CharField(max_length=150, null=False)
    pincode = models.CharField(max_length=150, null=False)
    area = models.CharField(max_length=150, null=False)
    house_name = models.CharField(max_length=150, null=False)
    total_price = models.FloatField(null=False)
    payment_mode = models.CharField(max_length=150, null=False)
    payment_id = models.FloatField(max_length=250, null=True)
    orderstatuses = (
        ('Pending','Pending'),
        ('Out for shipping', 'Out for shipping'),
        ('Compleated', 'Compleated')
    )
    status = models.CharField(max_length=150, choices = orderstatuses, default='Pending')
    message = models.TextField(null=True)
    tracking_no = models.CharField(max_length=150, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.id, self.tracking_no)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    price = models.FloatField(null=False)
    quantity = models.IntegerField(null=False)

    def __str__(self):
        return '{} - {}'.format(self.order.id, self.order.tracking_no)
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=150, null=False)
    city = models.CharField(max_length=150, null=False)
    pincode = models.CharField(max_length=150, null=False)
    area = models.CharField(max_length=150, null=False)
    house_name = models.CharField(max_length=150, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        self.user.username
    
class slide1(models.Model):
    slug = models.CharField(max_length=150, null=True, blank=False)
    name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to = get_file_path, null=True, blank=True)
    def __str__(self):
        return self.name    
class slide2(models.Model):
    slug = models.CharField(max_length=150, null=True, blank=False)
    name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to = get_file_path, null=True, blank=True)
    def __str__(self):
        return self.name
class slide3(models.Model):
    slug = models.CharField(max_length=150, null=True, blank=False)
    name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to = get_file_path, null=True, blank=True)
    def __str__(self):
        return self.name
class slide4(models.Model):
    slug = models.CharField(max_length=150, null=True, blank=False)
    name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to = get_file_path, null=True, blank=True)

    def __str__(self):
        return self.name