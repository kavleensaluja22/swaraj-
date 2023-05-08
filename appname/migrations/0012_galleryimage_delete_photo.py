# Generated by Django 4.1.5 on 2023-02-16 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0011_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery/')),
                ('caption', models.CharField(blank=True, max_length=100)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='photo',
        ),
    ]
