# Generated by Django 4.0.4 on 2022-05-20 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_alter_property_managers'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='property',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='property',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='description',
            field=models.TextField(max_length=12000),
        ),
        migrations.AlterField(
            model_name='property',
            name='image',
            field=models.ImageField(upload_to='propery/'),
        ),
        migrations.AlterField(
            model_name='property',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='property',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='property',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
