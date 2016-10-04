from django.contrib import admin

from .models import UserProfile, ParentOrder

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(ParentOrder)