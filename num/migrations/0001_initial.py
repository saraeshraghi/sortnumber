# Generated by Django 4.1.2 on 2022-10-14 05:34

from django.db import migrations, models
import num.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Numbers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_1', models.CharField(default='1', max_length=3)),
                ('num_2', models.CharField(default='random_string', max_length=3)),
                ('num_3', models.CharField(default='random_string', max_length=3)),
                ('num_4', models.CharField(default='random_string', max_length=3)),
                ('num_5', models.CharField(default='random_string', max_length=3)),
                ('num_6', models.CharField(default='random_string', max_length=3)),
                ('num_7', models.CharField(default='random_string', max_length=3)),
                ('num_8', models.CharField(default='random_string', max_length=3)),
                ('num_9', models.CharField(default='random_string', max_length=3)),
                ('num_10', models.CharField(default=num.models.random_string, max_length=3)),
            ],
        ),
    ]