from django.db import models
import datetime

class Home(models.Model):
    id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=30, null=False, default='아파트')
    home_No = models.IntegerField(null=False, default=0)
    message = models.TextField(default = "특별한 일정이 없습니다.")
    sensor_starttime = models.DateTimeField(null=False, default=datetime.datetime.now)
    sensor_endtime = models.DateTimeField(null=False, default=datetime.datetime.now)
    message_starttime = models.DateTimeField(null=False, default=datetime.datetime.now)
    message_endtime = models.DateTimeField(null=False, default=datetime.datetime.now)
    class Meta:
        db_table = 'Home'

class Status(models.Model):
    id = models.AutoField(primary_key = True)
    home_id = models.ForeignKey(Home, to_field='id', on_delete=models.CASCADE)
    noise = models.FloatField(default = 0)
    vibration = models.FloatField(default = 0)
    time = models.DateTimeField(null=False, default=datetime.datetime.now)

    class Meta:
        db_table = 'Status'

class Notice(models.Model):
    id = models.AutoField(primary_key = True)
    starttime = models.DateTimeField(null=False, default=datetime.datetime.now)
    endtime = models.DateTimeField(null=False, default=datetime.datetime.now)
    contents = models.TextField(default = "특별한 공지사항은 없습니다.")
    home_id = models.ForeignKey(Home, to_field='id', on_delete=models.CASCADE, default=1)

    class Meta:
        db_table = 'Notice'