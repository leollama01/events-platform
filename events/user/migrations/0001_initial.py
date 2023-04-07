# Generated by Django 4.2 on 2023-04-07 22:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default=None, max_length=120)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('local', models.CharField(default=None, max_length=60)),
                ('description', models.CharField(blank=True, max_length=60, null=True)),
                ('free_space', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
                'db_table': 'event',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('value', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('status', models.BooleanField(default=False)),
                ('method', models.CharField(choices=[('CA', 'Cash'), ('CC', 'Credit Card'), ('DC', 'Debit Card')], default='CA', max_length=2)),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
                'db_table': 'payment',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default=None, max_length=120)),
                ('age', models.IntegerField(default=None)),
                ('country', models.CharField(default=None, max_length=50)),
                ('state', models.CharField(default=None, max_length=50)),
                ('city', models.CharField(default=None, max_length=50)),
                ('phone_number', models.CharField(default=None, max_length=16)),
                ('email', models.CharField(default=None, max_length=80)),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'db_table': 'user',
                'ordering': ('id',),
            },
        ),
    ]
