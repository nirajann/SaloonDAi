# Generated by Django 4.0.1 on 2022-02-13 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data_field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=200)),
                ('user_id', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('Time', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'details',
            },
        ),
        migrations.CreateModel(
            name='history_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('order', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('customer_name', models.CharField(max_length=200)),
                ('Time', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'history',
            },
        ),
    ]
