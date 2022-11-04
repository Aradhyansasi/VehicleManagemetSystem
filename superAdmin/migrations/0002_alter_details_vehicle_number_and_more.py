# Generated by Django 4.1.3 on 2022-11-03 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superAdmin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='vehicle_number',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='vehicle_type',
            field=models.CharField(choices=[('Two Wheelers', 'Two Wheelers'), ('Three Wheelers', 'three Wheelers'), ('Four Wheelers', 'Four Wheelers')], default='Two Wheelers', max_length=50),
        ),
    ]