# Generated by Django 2.2.3 on 2019-08-30 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20190830_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='name',
            field=models.CharField(default='아파트', max_length=30),
        ),
    ]