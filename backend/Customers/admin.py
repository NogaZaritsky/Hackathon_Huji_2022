from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
  list = ('CustomerId','Name', 'email', 'other')

admin.site.register(Customer, CustomerAdmin)