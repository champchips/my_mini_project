# Generated by Django 3.0.3 on 2020-03-08 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20200308_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='picture',
            field=models.ImageField(upload_to='polls_image/'),
        ),
    ]