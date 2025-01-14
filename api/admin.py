from django.contrib import admin
from api.models import CustomUser, Profile
# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']

class ProfileAdmin(admin.ModelAdmin):
    list_editable = ['is_verified', 'full_name']
    list_display = ['user', 'full_name', 'is_verified']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile, ProfileAdmin)