# Generated by Django 4.0.3 on 2022-03-22 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='name')),
                ('description', models.TextField(max_length=200, verbose_name='description')),
                ('category', models.CharField(max_length=50)),
                ('price', models.IntegerField(verbose_name='price')),
                ('rating', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=200)),
                ('price', models.IntegerField(verbose_name='service_price')),
            ],
        ),
    ]
