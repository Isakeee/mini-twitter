from django.contrib import admin
from .models import (
    Category, 
    Article,
)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}