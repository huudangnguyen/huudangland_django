# Generated by Django 4.0.3 on 2022-03-28 04:10

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
                ('title', models.CharField(default='', max_length=255)),
                ('price', models.IntegerField(default=0)),
                ('classify', models.CharField(default='', max_length=50)),
                ('land_area', models.FloatField(default=0.0)),
                ('address', models.CharField(default='', max_length=255)),
                ('location_house', models.CharField(default='', max_length=50, null=True)),
                ('description', models.CharField(default='', max_length=255)),
                ('image', models.CharField(default='', max_length=255)),
            ],
        ),
    ]