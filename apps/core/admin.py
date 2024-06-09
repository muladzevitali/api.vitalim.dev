from django.contrib import admin

from .models import User

admin.site.register(User)


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'phone_number')
