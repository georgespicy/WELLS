from atexit import register
from django.contrib import admin
from .models import Category, Todo

# Register your models here.@admin.register(Blog)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    pass