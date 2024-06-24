# Generated by Django 5.0.6 on 2024-06-24 06:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OverriddenRoomRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('overridden_rate', models.DecimalField(decimal_places=2, max_digits=8)),
                ('stay_date', models.DateField()),
                ('room_rate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.roomrate')),
            ],
            options={
                'db_table': 'overridden_room_rate',
            },
        ),
    ]
