# Generated by Django 3.0.3 on 2020-03-09 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20200309_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='picture',
            field=models.FileField(upload_to='documents/%Y/%m/%d'),
        ),
    ]
