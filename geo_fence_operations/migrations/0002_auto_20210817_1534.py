# Generated by Django 3.2.6 on 2021-08-17 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo_fence_operations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geofence',
            name='lower_limit',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='geofence',
            name='upper_limit',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
