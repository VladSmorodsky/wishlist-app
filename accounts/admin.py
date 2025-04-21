from django.contrib import admin
from accounts.models import User


# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_staff', 'is_superuser')
    search_fields = ['email']
