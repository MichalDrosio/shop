from django.contrib import admin


from .models import ProfileUser


# Register your models here.

@admin.register(ProfileUser)
class ProfileUserAdmin(admin.ModelAdmin):
    list_display = ['user', 'street', 'postal_code','city', 'date_of_birth']