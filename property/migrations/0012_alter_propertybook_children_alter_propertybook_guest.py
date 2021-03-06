# Generated by Django 4.0.4 on 2022-05-24 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_remove_propertybook_count_propertybook_children_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertybook',
            name='children',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], default=0),
        ),
        migrations.AlterField(
            model_name='propertybook',
            name='guest',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], default=1),
        ),
    ]
