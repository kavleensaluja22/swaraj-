# Generated by Django 4.1.5 on 2023-02-16 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0010_alter_feedback_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
