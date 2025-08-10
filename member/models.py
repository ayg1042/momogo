from django.db import models

# Create your models here.
class Member(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    pw = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    nicname = models.CharField(max_length=20)
    mdate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id
    

class Friend(models.Model):
    # 친구 관계의 한쪽
    from_member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='friendships')
    # 친구 관계의 다른 쪽
    to_member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='friends_with')
    # 친구 추가 일시
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # 같은 관계 중복 방지
        unique_together = ('from_member', 'to_member')

    def __str__(self):
        return f"{self.from_member.id} → {self.to_member.id}"