# Generated by Django 4.1.5 on 2023-02-14 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0004_contact_delete_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='contact',
            new_name='feedback',
        ),
    ]
