# Generated by Django 3.2.4 on 2021-07-11 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KrishiSahayak', '0004_alter_shopupload_productpic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodorder',
            name='quantity',
            field=models.PositiveIntegerField(max_length=100000),
        ),
    ]