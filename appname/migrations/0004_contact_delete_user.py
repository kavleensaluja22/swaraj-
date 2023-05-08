# Generated by Django 4.1.5 on 2023-02-14 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=12)),
            ],
        ),
        migrations.DeleteModel(
            name='user',
        ),
    ]