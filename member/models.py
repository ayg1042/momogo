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