from django.db import models

# Create your models here.
class Bapgo(models.Model):
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=20)
    rate = models.FloatField(default=0)
    rcount = models.IntegerField(default=0)
    status = models.CharField(max_length=15)
    purl = models.TextField()
    Bdate = models.DateTimeField(auto_now=True)
    # 고유번호가 있으면 좋은데.


class Reviews(models.Model):
    # Bapgo - 고유번호
    rdate = models.DateField(auto_now=False)
    rrate = models.FloatField(default=0)
    rtext = models.TextField()


class KAKAO_API_TE(models.Model):
    kakao_id = models.CharField(max_length=50, primary_key=True)  # Kakao ID (Primary Key)
    place_name = models.CharField(max_length=255)  # 장소 이름
    road_address_name = models.CharField(max_length=500, blank=True, null=True)  # 도로명 주소
    latitude = models.FloatField()  # 위도
    longitude = models.FloatField()  # 경도
    created_at = models.DateTimeField(auto_now_add=True)  # 데이터 저장 시간

    def __str__(self):
        return self.place_name


class GOOGLE_API_TE(models.Model):
    kakao_id = models.OneToOneField(KAKAO_API_TE, on_delete=models.CASCADE, related_name='google_data')  # KAKAO_API_TE와 연결
    google_id = models.CharField(max_length=255, primary_key=True)  # Google API에서 반환된 고유 ID
    name = models.CharField(max_length=255)  # Google API에서 반환된 장소 이름
    type = models.CharField(max_length=255)  # Google API에서 반환된 장소 유형
    rating = models.FloatField(null=True, blank=True)  # 평균 사용자 평점
    address = models.CharField(max_length=500, null=True, blank=True)  # Google API에서 반환된 주소
    latitude = models.FloatField(null=True, blank=True)  # Google에서 반환된 위도
    longitude = models.FloatField(null=True, blank=True)  # Google에서 반환된 경도
    open_now = models.BooleanField(null=True, blank=True)  # 현재 열려있는지 여부
    phone = models.CharField(max_length=50, null=True, blank=True)  # 전화번호
    price_level = models.IntegerField(null=True, blank=True)  # 가격 수준 (0 ~ 4)
    user_ratings_total = models.IntegerField(null=True, blank=True)  # 총 사용자 평점 수
    pictures = models.JSONField(null=True, blank=True)  # 사진 URL 리스트
    reviews = models.JSONField(null=True, blank=True)  # 리뷰 리스트
    created_at = models.DateTimeField(auto_now_add=True)  # 데이터 저장 시간

    def __str__(self):
        return self.name