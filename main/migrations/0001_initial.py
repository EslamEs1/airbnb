# Generated by Django 4.0.4 on 2022-05-19 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('email', models.EmailField(max_length=50, verbose_name='Email')),
                ('subject', models.CharField(max_length=50, verbose_name='Subject')),
                ('message', models.TextField(max_length=500, verbose_name='Message')),
            ],
            options={
                'verbose_name_plural': 'Contact',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=30, verbose_name='Site Name')),
                ('logo', models.ImageField(upload_to='logo', verbose_name='Logo')),
                ('description', models.TextField(max_length=500, verbose_name='Description')),
                ('address', models.TextField(max_length=50, verbose_name='Address')),
                ('phone', models.CharField(max_length=20, verbose_name='Phone')),
                ('email', models.EmailField(max_length=50, verbose_name='Email')),
                ('facebook', models.URLField(blank=True, max_length=50, null=True, verbose_name='Facebook')),
                ('twitter', models.URLField(blank=True, max_length=50, null=True, verbose_name='Twitter')),
                ('instagram', models.URLField(blank=True, max_length=50, null=True, verbose_name='Instagram')),
            ],
            options={
                'verbose_name_plural': 'Website',
            },
        ),
    ]
