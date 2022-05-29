# Generated by Django 4.0.4 on 2022-05-29 20:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='profile_pic',
        ),
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]