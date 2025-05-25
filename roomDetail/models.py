from django.db import models
from room.models import ROOMS
from member.models import Member

# Create your models here.
class ROOM_DETAIL(models.Model):
    # 방번호
    room_id = models.ForeignKey(ROOMS, on_delete=models.CASCADE)
    # 유저
    user_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    user_status = models.IntegerField()

    # 반응 1~10
    reaction_00 = models.IntegerField()
    reaction_01 = models.IntegerField()
    reaction_02 = models.IntegerField()
    reaction_03 = models.IntegerField()
    reaction_04 = models.IntegerField()
    reaction_05 = models.IntegerField()
    reaction_06 = models.IntegerField()
    reaction_07 = models.IntegerField()
    reaction_08 = models.IntegerField()
    reaction_09 = models.IntegerField()

    def str(self):
        return f"Participant {self.id} in group {self.room_id.id}" 
