from django.contrib import admin

from api.models import Company 

class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
    )
    search_fields = ("name", "email", "tax_code")

admin.site.register(Company, CompanyAdmin)