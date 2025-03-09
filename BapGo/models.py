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