# Generated by Django 3.0.6 on 2020-05-30 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagramapp', '0003_auto_20200530_0353'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='location',
            field=models.CharField(default='Nairobi,Kenya', max_length=30),
        ),
    ]
