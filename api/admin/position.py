from django.contrib import admin
from api.models import Position

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("title", "is_manager", "is_active")