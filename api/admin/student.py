from django.contrib import admin

from api.models import Student 

class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "birth_date",
        "phone_number",
        "created_at",
        "updated_at",
    )
    search_fields = ("first_name", "last_name", "phone_number")
    list_filter = ("created_at", "updated_at")
    ordering = ("-created_at",)


admin.site.register(Student, StudentAdmin)