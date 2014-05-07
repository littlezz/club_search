from django.contrib import admin

# Register your models here.
from .models import UserProfile,GroupProfile

class UserProfileAdmin(admin.ModelAdmin):
    pass
admin.site.register(UserProfile,UserProfileAdmin)

class GroupProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(GroupProfile,GroupProfileAdmin)