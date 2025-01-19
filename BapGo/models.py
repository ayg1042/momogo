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