from django.contrib import admin
from .models import *

# Register your models here.


class ListNameAdmin(admin.ModelAdmin):
    list_display = ['list_name', 'user']


class ListItemAdmin(admin.ModelAdmin):
    list_display = ['list_item', 'list_n', 'user']


admin.site.register(ListName, ListNameAdmin)
admin.site.register(ListItem, ListItemAdmin)
