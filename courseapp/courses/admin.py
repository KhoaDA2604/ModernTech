from django.contrib import admin
from .models import Category,Course


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']
    list_filter = ['id', 'name']
    search_fields = ['pk', 'name']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Course)
