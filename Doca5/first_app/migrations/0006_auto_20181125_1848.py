# Generated by Django 2.1.3 on 2018-11-25 13:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0005_auto_20181125_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='date',
            field=models.DateField(default=datetime.datetime(2018, 11, 25, 18, 48, 16, 899533)),
        ),
    ]
