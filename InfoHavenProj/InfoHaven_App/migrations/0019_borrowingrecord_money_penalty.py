# Generated by Django 4.2.5 on 2023-12-02 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InfoHaven_App', '0018_borrowingrecord_penalty'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowingrecord',
            name='money_penalty',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]
