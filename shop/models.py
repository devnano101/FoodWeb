import django
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=200)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name

        
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=30, default="") 
    desc = models.CharField(max_length=300, default="")
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    userId = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")
    timestamp = models.DateTimeField(default=timezone.now)

class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.update_desc



# class UserProfile(models.Model):
#     Profile_user = models.OneToOneField(User, on_delete=models.CASCADE)
#     profile_img  = models.ImageField(default = "images/default_format.png")
#     f_name = models.CharField(max_length=60)
#     l_name = models.CharField(max_length=60)
#     email = models.CharField(max_length=111)
#     address = models.CharField(max_length=200)
#     phone = models.CharField(max_length=20, default="")
#     password = models.CharField(max_length=30, default="")
#     timestamp = models.DateTimeField(default=timezone.now)

# @receiver(post_save, sender= User)
# def Updated_prof_signal(sender, instace, created, **kwargs):
#     if created:
#         UserProfile.objects.create(Profile_user=instace)
#         instace.userprofile.save()

