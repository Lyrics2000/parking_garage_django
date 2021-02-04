# Generated by Django 3.1 on 2021-02-02 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20210202_1441'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_payment', models.BooleanField(default=False)),
                ('paypal_payment', models.BooleanField(default=False)),
                ('terms_condition', models.BooleanField(default=False)),
                ('hours', models.IntegerField()),
                ('vehicle_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.vehicle')),
            ],
        ),
    ]
