# Generated by Django 2.2.3 on 2019-09-01 00:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20190831_0927'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='home_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.Home'),
        ),
    ]
