from django.contrib import admin

from . models import Slider
# Register your models here.
@admin.register(Slider)
class NavbarMenuAdmin(admin.ModelAdmin):
    name_display = ('proName',)
    search_fields=('proName',)