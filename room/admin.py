from django.contrib import admin
from room.models import ROOMS

# Register your models here.
@admin.register(ROOMS)
class RoomsAdmin(admin.ModelAdmin):
    list_display = ['userId',
                    'place_01_id',
                    'place_02_id',
                    'place_03_id',
                    'place_04_id',
                    'place_05_id',
                    'place_06_id',
                    'place_07_id',
                    'place_08_id',
                    'place_09_id',
                    'place_10_id',
                    'status',
                    'search_area',
                    'search_keyword',
                    'Creation_time',
                    'place_personality',
                    ]