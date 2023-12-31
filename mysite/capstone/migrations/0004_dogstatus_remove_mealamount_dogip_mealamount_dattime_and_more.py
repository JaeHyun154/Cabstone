# Generated by Django 4.2.6 on 2023-11-30 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capstone', '0003_alter_mealamount_options_alter_mealamount_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='DogStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(blank=True, max_length=100, null=True)),
                ('walking', models.FloatField(blank=True, null=True)),
                ('resting', models.FloatField(blank=True, null=True)),
                ('running', models.FloatField(blank=True, null=True)),
                ('accumulatedMeal', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'DogStatus',
                'managed': True,
            },
        ),
        migrations.RemoveField(
            model_name='mealamount',
            name='dogip',
        ),
        migrations.AddField(
            model_name='mealamount',
            name='DatTime',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterModelTable(
            name='activity',
            table='Activity',
        ),
    ]
