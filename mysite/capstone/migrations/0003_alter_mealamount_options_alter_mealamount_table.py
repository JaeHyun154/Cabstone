# Generated by Django 4.2.6 on 2023-11-05 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('capstone', '0002_mealamount'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mealamount',
            options={'managed': True},
        ),
        migrations.AlterModelTable(
            name='mealamount',
            table='mealAmount',
        ),
    ]