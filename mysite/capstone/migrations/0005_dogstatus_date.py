# Generated by Django 4.2.6 on 2023-11-30 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capstone', '0004_dogstatus_remove_mealamount_dogip_mealamount_dattime_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dogstatus',
            name='Date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
