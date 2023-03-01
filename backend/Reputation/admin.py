from django.contrib import admin

# Register your models here.
from . models import Reputation
# Register your models here.
@admin.register(Reputation)
class NavbarMenuAdmin(admin.ModelAdmin):
    name_display = ('name',)
    search_fields=('name',)