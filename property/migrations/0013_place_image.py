# Generated by Django 4.0.4 on 2022-05-29 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_alter_propertybook_children_alter_propertybook_guest'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='image',
            field=models.ImageField(default='he', upload_to='Place/images/'),
            preserve_default=False,
        ),
    ]
