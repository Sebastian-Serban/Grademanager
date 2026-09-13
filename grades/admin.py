from django.contrib import admin

from .models import Grade


# Register your models here.
@admin.register(Grade)
class PostAdmin(admin.ModelAdmin):
    list_display = ["grade", "created_at", "updated_at"]
