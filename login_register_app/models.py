# from __future__ import unicode_literals
from django.db import models
from datetime import date, datetime
import re

class UserManager(models.Manager):
    def basic_validator(self, post_data):    
        errors = {}
        name_regex = re.compile(r'^[a-zA-Z\s]+$')
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if not name_regex.match(post_data['first_name']):        
            errors['first_name'] = "First name must be letters."
        if len(post_data['first_name']) < 2:
            errors['first_name'] = 'First name not long enough'

        if not name_regex.match(post_data['last_name']):        
            errors['last_name'] = "Last name must be letters."
        if len(post_data['last_name']) < 2:
            errors['last_name'] = 'Last name not long enough'

        if not email_regex.match(post_data['email']):          
            errors['email'] = "Invalid email address!"
        if len(User.objects.filter(email = post_data['email'])) != 0:
            errors['email'] = 'Email is already in use.'

        if len(post_data['password']) < 8 :               
            errors['password_length'] = "Invalid password!"
        if (post_data['password']) != (post_data['confirm_password']) :               
            errors['password_match'] = "Did not confirm password!"

        return errors

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 320)
    password = models.CharField(max_length = 60)
    shoe_size = models.FloatField(null=True)
    shipping_address = models.CharField(max_length = 255, null=True)
    shipping_city = models.CharField(max_length = 255, null=True)
    shipping_zip = models.IntegerField(null=True)
    billing_address = models.CharField(max_length = 255, null=True)
    billing_city = models.CharField(max_length = 255, null=True)
    billing_zip = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


class InventoryManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        if len(Inventory.objects.filter(item_brand = post_data['item_brand'])) != 0:
            errors['item_brand'] = 'Item Brand not long enough.'
        if len(Inventory.objects.filter(item_name = post_data['item_name'])) != 0:
            errors['item_name'] = 'Item Name not long enough.'
        if len(Inventory.objects.filter(condition = post_data['condition'])) != 0:
            errors['condition'] = 'Conditon must be filled out.'
        return errors

class Inventory(models.Model):
    item_brand = models.CharField(max_length = 255)
    item_name = models.CharField(max_length = 255)
    item_primary_color = models.CharField(max_length = 255)
    item_secondary_color = models.CharField(max_length = 255, null=True)
    item_price = models.FloatField(default="50")
    front_img = models.ImageField(upload_to='uploads')
    back_img = models.ImageField(upload_to='uploads')
    top_img = models.ImageField(upload_to='uploads')
    bottom_img = models.ImageField(upload_to='uploads')
    left_img = models.ImageField(upload_to='uploads')
    right_img = models.ImageField(upload_to='uploads')
    condition = models.CharField(max_length = 255)
    item_size = models.FloatField()
    item_gender = models.CharField(max_length = 255)
    availability = models.BooleanField(default=True)
    buyer = models.ForeignKey(User, related_name="bought", on_delete = models.CASCADE, null=True)
    seller = models.ForeignKey(User, related_name="sold", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)





# class Photo(models.Model):
#     inventory_img = models.ImageField(upload_to='images/')
#     Photo = models.ForeignKey(Inventory, related_name="item_photos", on_delete = models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)



