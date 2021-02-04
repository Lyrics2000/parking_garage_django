# Generated by Django 3.1 on 2021-02-02 02:56

from django.db import migrations, models
import django.db.models.deletion
import mainapp.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20210201_1315'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParkingSlots',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parking_area_name', models.CharField(max_length=100)),
                ('parking_cost_per_hour', models.IntegerField()),
                ('parking_location', models.CharField(max_length=150)),
                ('parking_facility', models.CharField(choices=[('PR', 'Parking Facility'), ('OS', 'Open Space')], max_length=300)),
                ('security_inclusive', models.BooleanField(default=False)),
                ('carwash_available', models.BooleanField(default=False)),
                ('nearby_restaurant', models.BooleanField(default=False)),
                ('parking_picture', models.FileField(null=True, upload_to=mainapp.models.upload_image_path)),
                ('parking_overview', models.TextField(blank=True, null=True)),
                ('booked', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True, default=uuid.uuid4, unique=True)),
                ('parking_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.parking')),
            ],
        ),
    ]
