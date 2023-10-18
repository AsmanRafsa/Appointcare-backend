# Generated by Django 4.2.6 on 2023-10-18 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_Name', models.CharField(max_length=60)),
                ('hospital_Image', models.ImageField(upload_to='')),
                ('hospital_Location', models.CharField(max_length=60)),
                ('hospital_Slogan', models.CharField(max_length=100)),
                ('hospital_Detail', models.TextField()),
            ],
        ),
    ]
