# Generated by Django 4.0.3 on 2022-04-07 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customers', '0002_rename_preferred_study_habits_customer_preferred_study_habits_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='home',
            field=models.IntegerField(),
        ),
    ]
