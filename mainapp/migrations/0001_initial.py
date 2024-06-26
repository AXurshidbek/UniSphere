# Generated by Django 5.0.4 on 2024-04-27 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Center',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('description', models.TextField()),
                ('profile_pic', models.FileField(upload_to='')),
                ('phone_num1', models.CharField(max_length=15)),
                ('phone_num2', models.CharField(blank=True, max_length=15, null=True)),
                ('phone_num3', models.CharField(blank=True, max_length=15, null=True)),
                ('adress', models.TextField()),
                ('map_location', models.CharField(max_length=500)),
                ('websyte', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Pictures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
            ],
        ),
    ]
