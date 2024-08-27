from django.contrib import admin
from usersapp.models import User
from .models import Profile

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name','last_name','other_names','address', 'phone', 'alt_phone', 'profile_pic' ]

admin.site.register(User, UserAdmin)
admin.site.register( Profile,ProfileAdmin)
