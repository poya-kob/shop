# Generated by Django 3.2.7 on 2021-10-26 12:57

from django.db import migrations, models
import settings.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=500)),
                ('phone', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=50)),
                ('fax', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('about_us', models.TextField(blank=True, null=True)),
                ('copy_right', models.CharField(blank=True, max_length=200, null=True)),
                ('logo_image', models.ImageField(upload_to=settings.models.upload_image_path)),
            ],
        ),
    ]