from django.contrib import admin
from .models import Blog, BlogCategory  

class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class BlogAdmin(admin.ModelAdmin):
    exclude = ('created_at',)
    list_display = ('name', 'category', 'description', 'status')

admin.site.register(BlogCategory, BlogCategoryAdmin)
admin.site.register(Blog, BlogAdmin)
