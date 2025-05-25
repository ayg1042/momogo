from django.contrib import admin
from BapGo.models import Bapgo, Reviews, GOOGLE_API_TE, KAKAO_API_TE

# Register your models here.

@admin.register(Bapgo)
class BapgoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category']

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'rdate', 'rrate', 'rtext']

@admin.register(KAKAO_API_TE)
class KAKAO_API_TE(admin.ModelAdmin):
    list_display = ['kakao_id', 'place_name', 'road_address_name', 'latitude', 'longitude', 'created_at']

@admin.register(GOOGLE_API_TE)
class GOOGLE_API_TE(admin.ModelAdmin):
    list_display = ['kakao_id', 'google_id', 'name', 'type', 'rating', 'address', 'latitude', 'longitude', 'open_now', 'phone', 'price_level', 'user_ratings_total', 'pictures', 'reviews', 'created_at']