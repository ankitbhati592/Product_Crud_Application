from django.contrib import admin

from .models import Product

class productAdmin(admin.ModelAdmin):
	list_display=['productName','price', 'user']

admin.site.register(Product,productAdmin)
