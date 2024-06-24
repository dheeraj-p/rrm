# Generated by Django 5.0.6 on 2024-06-24 12:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_discount_discount_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='discount_type',
            field=models.CharField(choices=[('fixed', 'Fixed'), ('percentage', 'Percentage')], default='fixed', max_length=10),
        ),
        migrations.CreateModel(
            name='DiscountRoomRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.discount')),
                ('room_rate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.roomrate')),
            ],
            options={
                'db_table': 'discount_room_rate',
            },
        ),
    ]
