from django.contrib import admin
from .models import User,Follwing
# Register your models here.
admin.site.register(Follwing)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ["username", "first_name", "last_name", "verified", "email"]
    search_fields = ["username", "first_name", "last_name"]