# Generated by Django 2.1 on 2020-12-04 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=20)),
                ('ID', models.IntegerField(blank=True, max_length=5, unique=True)),
                ('Address', models.TextField(blank=True, max_length=20)),
            ],
        ),
    ]
