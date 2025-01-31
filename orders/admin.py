# filepath: /home/danial/projects/Doni/cargo_transport/orders/admin.py
from django.contrib import admin
from .models import Profile, Order, Driver

admin.site.register(Profile)
admin.site.register(Order)
admin.site.register(Driver)