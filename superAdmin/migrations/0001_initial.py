# Generated by Django 4.1.3 on 2022-11-03 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_number', models.CharField(max_length=50)),
                ('vehicle_type', models.CharField(max_length=50)),
                ('vehicle_model', models.CharField(max_length=50)),
                ('vehicle_description', models.CharField(max_length=100)),
            ],
        ),
    ]
