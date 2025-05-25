from django.contrib import admin
from .models import ROOM_DETAIL

@admin.register(ROOM_DETAIL)
class ROOM_DETAILAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'room_id',
        'user_id',
        'user_status',
        'reaction_00',
        'reaction_01',
        'reaction_02',
        'reaction_03',
        'reaction_04',
        'reaction_05',
        'reaction_06',
        'reaction_07',
        'reaction_08',
        'reaction_09',
    )
