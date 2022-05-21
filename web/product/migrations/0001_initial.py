# Generated by Django 4.0.3 on 2022-05-16 13:31

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
                ('price', models.IntegerField(default=0, null=True)),
                ('area', models.FloatField(default=0.0)),
                ('address', models.CharField(default='', max_length=255)),
                ('location_house', models.IntegerField(default=0)),
                ('floors', models.IntegerField(default=0)),
                ('to_center', models.FloatField(default=0.0)),
                ('image', models.TextField(default='')),
                ('price_predict', models.IntegerField(default=0, null=True)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
