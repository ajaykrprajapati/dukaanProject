from django.db import models
from django.core import validators
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib import auth
from random import randint
from django.utils.text import slugify


class Account(auth.models.User):
    is_deleted = models.BooleanField(default=False)
    created_at_utc = models.DateTimeField(auto_now_add=True)
    modified_at_utc = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = "Account"
        ordering = ("-created_at_utc",)


class Store(models.Model):
    store_name = models.CharField(max_length=256, null=False, blank=False)
    address = models.CharField(max_length=500, null=False, blank=False)
    owner = models.ForeignKey(Account, on_delete=models.CASCADE)
    slug = models.SlugField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    created_at_utc = models.DateTimeField(auto_now_add=True)
    modified_at_utc = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.store_name

    class Meta:
        db_table = "Store"
        ordering = ("-created_at_utc",)

    def save(self, *args, **kwargs):
        if Store.objects.filter(store_name=self.store_name).exists():
            extra = str(randint(1, 10000))
            self.slug = slugify(self.store_name) + "-" + extra
        else:
            self.slug = slugify(self.store_name)
        super(Store, self).save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=255, default="New")
    is_deleted = models.BooleanField(default=False)
    created_at_utc = models.DateTimeField(auto_now_add=True)
    modified_at_utc = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Category"
        ordering = ("-created_at_utc",)
