# Generated by Django 4.1.2 on 2022-10-07 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cars", "0004_alter_car_description_alter_car_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="description",
            field=models.TextField(max_length=500),
        ),
    ]
