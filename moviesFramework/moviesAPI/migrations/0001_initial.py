# Generated by Django 3.2.6 on 2021-08-17 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movies',
            fields=[
                ('movName', models.CharField(max_length=20)),
                ('movDiscp', models.CharField(max_length=100)),
                ('mov_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
