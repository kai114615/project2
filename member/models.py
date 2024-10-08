from django.db import models
from datetime import datetime

# Create your models here.
class Member(models.Model):
    member_id = models.AutoField(primary_key=True)
    member_name = models.CharField(max_length=20, unique=True)
    member_password = models.CharField(max_length=128)  # 密碼會加密，所以長度較長
    member_birth = models.DateField()
    member_email = models.EmailField(max_length=200, unique=True, default='')
    member_avatar = models.CharField(max_length=100, default='istockphoto-2132177453-612x612.jpg')
    last_update = models.DateTimeField(default=datetime.now())

    class Meta:
        db_table = 'member'  # 指定的資料表名稱

