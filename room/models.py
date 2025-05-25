from django.db import models
from member.models import Member
from BapGo.models import GOOGLE_API_TE

# Create your models here.
class ROOMS(models.Model):
    # 방장(생성자)
    add_who = models.ForeignKey(Member, on_delete=models.CASCADE)
    place_00_id = models.ForeignKey(GOOGLE_API_TE, on_delete=models.CASCADE)
    place_01_id = models.ForeignKey(GOOGLE_API_TE, on_delete=models.CASCADE)
    place_02_id = models.ForeignKey(GOOGLE_API_TE, on_delete=models.CASCADE)
    place_03_id = models.ForeignKey(GOOGLE_API_TE, on_delete=models.CASCADE)
    place_04_id = models.ForeignKey(GOOGLE_API_TE, on_delete=models.CASCADE)
    place_05_id = models.ForeignKey(GOOGLE_API_TE, on_delete=models.CASCADE)
    place_06_id = models.ForeignKey(GOOGLE_API_TE, on_delete=models.CASCADE)
    place_07_id = models.ForeignKey(GOOGLE_API_TE, on_delete=models.CASCADE)
    place_08_id = models.ForeignKey(GOOGLE_API_TE, on_delete=models.CASCADE)
    place_09_id = models.ForeignKey(GOOGLE_API_TE, on_delete=models.CASCADE)
    # 상태
    status = models.CharField(max_length=1)
    # 검색 지역
    search_area = models.CharField(max_length=10)
    # 검색 키워드
    search_keyword = models.CharField(max_length=10)
    # 생성시점
    add_date = models.DateTimeField(auto_now_add=True)
    # 자리성격
    place_purpose = models.CharField(max_length=10)