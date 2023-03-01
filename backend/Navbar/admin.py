from django.contrib import admin

# Register your models here.
from . models import NavbarLogo,NavbarMenu

# admin.site.register(Course)
@admin.register(NavbarLogo)
class NavbarAdmin(admin.ModelAdmin):
    name_display = ('name',)
    search_fields=('name',)
    
@admin.register(NavbarMenu)
class NavbarMenuAdmin(admin.ModelAdmin):
    name_display = ('name',)
    search_fields=('name',)
    