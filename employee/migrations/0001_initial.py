# Generated by Django 5.0.7 on 2024-07-16 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('id', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=30)),
                ('cell_phone', models.CharField(max_length=30, null=True)),
                ('construction_hours', models.FloatField(default=0, max_length=30, null=True)),
                ('dismantling_hours', models.FloatField(default=0, max_length=30, null=True)),
                ('total_km', models.FloatField(default=0, null=True)),
                ('total_transport', models.FloatField(default=0, null=True)),
                ('total_food', models.FloatField(default=0, null=True)),
                ('total_parking', models.FloatField(default=0, null=True)),
                ('hourly_wage', models.FloatField(default=35, null=True)),
                ('salary', models.FloatField(default=0, null=True)),
                ('shift_start_date_time', models.DateTimeField(null=True)),
                ('shift_end_date_time', models.DateTimeField(null=True)),
            ],
        ),
    ]
