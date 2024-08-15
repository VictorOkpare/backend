from django.contrib import admin
from usersapp.models import User,Profile

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'address', 'mobile' ]

admin.site.register(User, UserAdmin)
admin.site.register( Profile,ProfileAdmin)
