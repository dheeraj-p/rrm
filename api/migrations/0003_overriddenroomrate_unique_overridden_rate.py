# Generated by Django 5.0.6 on 2024-06-24 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_overriddenroomrate'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='overriddenroomrate',
            constraint=models.UniqueConstraint(fields=('room_rate', 'stay_date'), name='unique_overridden_rate'),
        ),
    ]
