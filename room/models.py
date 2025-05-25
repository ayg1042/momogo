from django.db import models
from member.models import Member
from BapGo.models import GOOGLE_API_TE

# Create your models here.
class ROOMS(models.Model):
    add_who = models.ForeignKey(Member, on_delete=models.CASCADE)

    place_00_id = models.ForeignKey(GOOGLE_API_TE, on_delete=models.CASCADE, related_name='rooms_place_00')
    place_01_id = models.ForeignKey(GOOGLE_API_TE, on_delete=models.CASCADE, related_name='rooms_place_01')
    place_02_id = models.ForeignKey(GOOGLE_API_TE, on_delete=models.CASCADE, related_name='rooms_place_02')
    place_03_id = models.ForeignKey(GOOGLE_API_TE, on_delete=models.CASCADE, related_name='rooms_place_03')
    place_04_id = models.ForeignKey(GOOGLE_API_TE, on_delete=models.CASCADE, related_name='rooms_place_04')
    place_05_id = models.ForeignKey(GOOGLE_API_TE, on_delete=models.CASCADE, related_name='rooms_place_05')
    place_06_id = models.ForeignKey(GOOGLE_API_TE, on_delete=models.CASCADE, related_name='rooms_place_06')
    place_07_id = models.ForeignKey(GOOGLE_API_TE, on_delete=models.CASCADE, related_name='rooms_place_07')
    place_08_id = models.ForeignKey(GOOGLE_API_TE, on_delete=models.CASCADE, related_name='rooms_place_08')
    place_09_id = models.ForeignKey(GOOGLE_API_TE, on_delete=models.CASCADE, related_name='rooms_place_09')

    status = models.CharField(max_length=1)
    search_area = models.CharField(max_length=10)
    search_keyword = models.CharField(max_length=10)
    add_date = models.DateTimeField(auto_now_add=True)
    place_purpose = models.CharField(max_length=10)

    def __str__(self):
        return f"Room by {self.add_who} at {self.add_date}"
