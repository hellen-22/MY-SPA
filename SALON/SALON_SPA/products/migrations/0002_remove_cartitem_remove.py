# Generated by Django 4.0.4 on 2022-05-09 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='remove',
        ),
    ]
