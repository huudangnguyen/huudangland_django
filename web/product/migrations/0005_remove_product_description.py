# Generated by Django 4.0.3 on 2022-04-04 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_rename_land_area_product_area_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
    ]