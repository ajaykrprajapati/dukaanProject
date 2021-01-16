from django.contrib import admin

# Register your models here.
from .models import Account, Store, Category

admin.site.register(Account)
admin.site.register(Store)
admin.site.register(Category)