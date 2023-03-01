from django.contrib import admin

# Register your models here.
from . models import AboutHeader,AboutFront,AboutExprience,PostImage

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
 
@admin.register(AboutExprience)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]
 
    class Meta:
       model = AboutExprience
 
# @admin.register(PostImage)
# class PostImageAdmin(admin.ModelAdmin):
#     pass