# Generated by Django 4.1.1 on 2022-11-09 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_band_like_new'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='band',
            name='like_new',
        ),
    ]
