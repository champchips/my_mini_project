# Generated by Django 3.0.3 on 2020-03-09 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20200310_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='password',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='poll',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
