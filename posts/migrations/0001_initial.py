# Generated by Django 4.2.5 on 2023-09-20 11:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='POST',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField(max_length=100000)),
                ('created_on', models.DateTimeField(blank=True, default=datetime.datetime(2023, 9, 20, 11, 5, 49, 77138))),
            ],
        ),
    ]
