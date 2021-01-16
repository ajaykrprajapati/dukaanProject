from django.db import models
from django.contrib import auth
from seller.models import Category, Store


class Product(models.Model):
    product_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    mrp = models.PositiveIntegerField()
    sales_price = models.PositiveIntegerField()
    image = models.CharField(max_length=255, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)
    created_at_utc = models.DateTimeField(auto_now_add=True)
    modified_at_utc = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.product_name

    class Meta:
        db_table = "Product"
        ordering = ("-created_at_utc",)


class Cart(models.Model):
    store_link = models.CharField(max_length=255)
    is_deleted = models.BooleanField(default=False)
    created_at_utc = models.DateTimeField(auto_now_add=True)
    modified_at_utc = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.store_link

    class Meta:
        db_table = "Cart"
        ordering = ("-created_at_utc",)


class ItemDetail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)
    created_at_utc = models.DateTimeField(auto_now_add=True)
    modified_at_utc = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.product

    class Meta:
        db_table = "ItemDetail"
        ordering = ("-created_at_utc",)


class Customer(auth.models.User):
    address = models.CharField(max_length=500)
    is_deleted = models.BooleanField(default=False)
    created_at_utc = models.DateTimeField(auto_now_add=True)
    modified_at_utc = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.address

    class Meta:
        db_table = "Customer"
        ordering = ("-created_at_utc",)


class Order(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE, related_name="order")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)
    created_at_utc = models.DateTimeField(auto_now_add=True)
    modified_at_utc = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.customer

    class Meta:
        db_table = "Order"
        ordering = ("-created_at_utc",)
