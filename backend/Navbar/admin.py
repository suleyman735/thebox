from django.contrib import admin

# Register your models here.
from . models import NavbarLogo

# admin.site.register(Course)
@admin.register(NavbarLogo)
class NavbarAdmin(admin.ModelAdmin):
    name_display = ('name',)
    search_fields=('name',)
    