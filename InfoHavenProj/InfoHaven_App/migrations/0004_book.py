# Generated by Django 4.2.5 on 2023-10-09 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InfoHaven_App', '0003_auto_20231001_2309'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.AutoField(primary_key=True, serialize=False)),
                ('author_id', models.CharField(max_length=50, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('publisher', models.CharField(max_length=255)),
                ('classification', models.CharField(max_length=255)),
                ('date_published', models.DateField()),
                ('isbn', models.CharField(max_length=13)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
    ]
