from django.contrib import admin
from .models import Post, Category

from mptt.admin import DraggableMPTTAdmin
from django_mptt_admin.admin import DjangoMpttAdmin 
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Админ-панель модели записи
    """
    prepopulated_fields = {'slug':('title',)}


@admin.register(Category)
class CategoryAdmin(DjangoMpttAdmin):
    """
    Админ панель модели категорий
    """
    prepopulated_fields = {'slug':('title',)}