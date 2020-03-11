# Generated by Django 3.0.3 on 2020-03-11 20:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0015_auto_20200310_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll_vote',
            name='count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='poll',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 12, 3, 20, 59, 23308)),
        ),
        migrations.AlterField(
            model_name='poll',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 12, 3, 20, 59, 22330)),
        ),
        migrations.AlterField(
            model_name='poll_choice',
            name='image',
            field=models.ImageField(upload_to='choice/%Y/%m/%d'),
        ),
    ]