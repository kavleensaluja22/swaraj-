# Generated by Django 4.1.5 on 2023-03-19 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0015_otp_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='otp',
            old_name='otp',
            new_name='otp_id',
        ),
    ]