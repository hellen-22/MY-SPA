# Generated by Django 4.0.6 on 2022-09-28 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_rename_unit_price_orderitem_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='price',
        ),
    ]
