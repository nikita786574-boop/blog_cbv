from django.contrib import admin
from .models import Post, Category

from mptt.admin import DraggableMPTTAdmin
from django_mptt_admin.admin import DjangoMpttAdmin 
# Register your models here.

admin.site.register(Post)

@admin.register(Category)
class CategoryAdmin(DjangoMpttAdmin):
    """
    Админ панель модели категорий
    """
    prepopulated_fields = {'slug':('title',)}