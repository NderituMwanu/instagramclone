# Generated by Django 3.0.6 on 2020-05-30 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagramapp', '0004_user_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.CharField(default='Nairobi,Kenya', max_length=30),
        ),
    ]
