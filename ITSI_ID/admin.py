from django.contrib import admin
from .models import Users, Products, Services, API

@admin.register(Users)
class Users(admin.ModelAdmin):
    list_display = ['name', 'surname']  

    def custom_name(self, obj):
        return obj.name

    custom_name.short_description = 'Name'

    def custom_surname(self, obj):
        return obj.surname

    custom_surname.short_description = 'Surname'

@admin.register(Products)
class Users(admin.ModelAdmin):
    list_display = ['name']  

    def custom_name(self, obj):
        return obj.name

    custom_name.short_description = 'Name'

@admin.register(Services)
class Users(admin.ModelAdmin):
    list_display = ['name']  

    def custom_name(self, obj):
        return obj.name

    custom_name.short_description = 'Name'

admin.site.register(API)

