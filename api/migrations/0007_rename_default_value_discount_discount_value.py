# Generated by Django 5.0.6 on 2024-06-24 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_discount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='discount',
            old_name='default_value',
            new_name='discount_value',
        ),
    ]