from django.contrib import admin
from BapGo.models import Bapgo, Reviews

# Register your models here.

@admin.register(Bapgo)
class BapgoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category']

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'rdate', 'rrate', 'rtext']