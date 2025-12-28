from django.contrib import admin
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    """博客文章后台管理"""
    list_display = ('title', 'owner', 'date_added')
    list_filter = ('date_added', 'owner')
    search_fields = ('title', 'text')
    ordering = ['-date_added']