from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'time_create', 'time_update', 'is_published')
    list_display_links = ('id', 'name',)
    search_fields = ('id', 'name', 'time_create', 'time_update', 'is_published')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('name',)}


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'time_create', 'time_update', 'is_published')
    list_display_links = ('id', 'name', 'email')
    search_fields = ('id', 'name', 'email', 'time_create', 'time_update', 'is_published')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'namePerson',  'category', 'price', 'phone', 'image', 'video', 'file', 'description', 'time_create', 'time_update', 'is_published')
    list_display_links = ('id', 'name', 'namePerson',)
    search_fields = ('id', 'name', 'namePerson', 'category', 'price', 'phone', 'email')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('name', )}


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ContactUsModel, ContactUsAdmin)