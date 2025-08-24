from django.contrib import admin
from .models import Category, Tag, Article

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ('name',)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'created_at', 'updated_at')
    list_filter = ('category', 'tags', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    raw_id_fields = ('author',)
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    filter_horizontal = ('tags',)
