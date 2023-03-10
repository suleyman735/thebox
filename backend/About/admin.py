from django.contrib import admin

# Register your models here.
from . models import AboutHeader,AboutFront,AboutExprience,PostImage,ProfesionalSection,CounterSelection

# admin.site.register(AboutHeader)
@admin.register(AboutHeader)
@admin.register(AboutFront)
# @admin.register(AboutExprience)
# @admin.site.register(Photo)

class AboutAdmin(admin.ModelAdmin):
    
    name_display = ('name',)
    search_fields=('name',)

class PostImageAdmin(admin.StackedInline):
    model = PostImage
    
class ProfesionalSectionAdmin(admin.StackedInline):
    model = ProfesionalSection
class CounterSelectionAdmin(admin.StackedInline):
    model = CounterSelection

@admin.register(AboutExprience)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin,ProfesionalSectionAdmin,CounterSelectionAdmin]
    class Meta:
       model = AboutExprience

 
# @admin.register(PostImage)
# class PostImageAdmin(admin.ModelAdmin):
#     pass