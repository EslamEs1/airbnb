# Generated by Django 4.0.4 on 2022-05-19 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='about/')),
                ('vision', models.TextField(max_length=10000, verbose_name='what_we_do')),
                ('mission', models.TextField(max_length=10000, verbose_name='our_mission')),
                ('goals', models.TextField(max_length=10000, verbose_name='our_goal')),
            ],
            options={
                'verbose_name': 'FAQ',
                'verbose_name_plural': 'About',
            },
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Title')),
                ('Description', models.TextField(max_length=1000, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'FAQ',
                'verbose_name_plural': 'FAQ',
            },
        ),
    ]
