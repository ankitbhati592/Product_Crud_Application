
from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models
from django.contrib.contenttypes.models import ContentType

from django.utils.encoding import python_2_unicode_compatible

class Product(models.Model):
	user = models.ForeignKey(User, blank=True, null=True)
	productName = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	quantity = models.IntegerField(max_length=20,default=0)
	price = models.IntegerField(max_length=20,default=0)
	phoneNumber = models.IntegerField(max_length=20,default=0)
	status = models.NullBooleanField()
	image = models.ImageField(upload_to="product/images/",default="none/product1.jpg")

# class Product_Image(models.Model):
# 	product_name=models.CharField(max_length=200)
# 	image_id=models.CharField(max_length=200)
# 	created_at=models.CharField(max_length=200)
# 	updated_at=models.CharField(max_length=200)
