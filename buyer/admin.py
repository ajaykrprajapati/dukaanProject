from django.contrib import admin
from .models import Product, ItemDetail, Cart, Order, Customer


# Register your models here.
admin.site.register(Product)
admin.site.register(ItemDetail)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Customer)
