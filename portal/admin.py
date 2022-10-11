from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Portal)
class PortalAdmin(admin.ModelAdmin):
    list_display = ('title', 'cat', 'time_create', 'time_update', 'is_published')
    list_editable = ('is_published',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
