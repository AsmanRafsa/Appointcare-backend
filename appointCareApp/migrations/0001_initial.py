# Generated by Django 4.2.6 on 2023-10-23 13:44

import appointCareApp.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=15, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='HospitalNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=100)),
                ('booked_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phoneNumber', models.CharField(max_length=150)),
                ('profilePic', models.ImageField(default='user/', upload_to=appointCareApp.models.upload_to, verbose_name='image')),
            ],
        ),
        migrations.CreateModel(
            name='HospitalDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_Image', models.ImageField(default='hospitals/mayoclinic.jpg', upload_to=appointCareApp.models.upload_to, verbose_name='image')),
                ('hospital_Location', models.CharField(max_length=60)),
                ('hospital_Slogan', models.CharField(blank=True, max_length=100)),
                ('hospital_Description', models.TextField()),
                ('hospital', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='appointCareApp.hospital')),
            ],
        ),
        migrations.CreateModel(
            name='DoctorsDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctorImage', models.ImageField(default='hospitals/default.jpg', upload_to=appointCareApp.models.upload_to, verbose_name='image')),
                ('doctorName', models.CharField(max_length=50)),
                ('doctorSpeciality', models.CharField(choices=[('cardiologist', 'Cardiologist'), ('dermatologist', 'Dermatologist'), ('neurologist', 'Neurologist'), ('pediatric', 'Pediatric')], max_length=50)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctors', to='appointCareApp.hospital')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientDisease', models.TextField()),
                ('patientAge', models.PositiveIntegerField()),
                ('timeBooked', models.DateTimeField(default=datetime.datetime(2023, 10, 23, 13, 44, 18, 960505, tzinfo=datetime.timezone.utc))),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
