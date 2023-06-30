from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *
# Register your models here.

admin.site.unregister(Group)

admin.site.register(Picture)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','type','description')
    search_fields = ('name','type')

    exclude = ('slug',)

admin.site.register(Category,CategoryAdmin)