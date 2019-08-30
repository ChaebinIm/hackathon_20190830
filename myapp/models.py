from django.db import models
import datetime

class Home(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, null=False, default='아파트')
    home_No = models.IntegerField(null=False, default=0)
    message = models.TextField(default = "특별한 일정이 없습니다.")
    isOn = models.IntegerField(default = 1)

    class Meta:
        db_table = 'Home'

class Status(models.Model):
    id = models.AutoField(primary_key = True)
    home_No = models.ForeignKey(Home, to_field='id', on_delete=models.CASCADE)
    noise = models.FloatField(default = 0)
    vibration = models.FloatField(default = 0)
    starttime = models.DateTimeField(null=False, default=datetime.datetime.now)
    endtime = models.DateTimeField(null=False, default=datetime.datetime.now)

    class Meta:
        db_table = 'Status'

class Notice(models.Model):
    id = models.AutoField(primary_key = True)
    starttime = models.DateTimeField(null=False, default=datetime.datetime.now)
    endtime = models.DateTimeField(null=False, default=datetime.datetime.now)
    contents = models.TextField(default = "특별한 공지사항은 없습니다.")

    class Meta:
        db_table = 'Notice'