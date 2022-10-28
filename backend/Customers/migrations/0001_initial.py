# Generated by Django 3.0.7 on 2022-04-07 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('family_name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('courses', models.CharField(max_length=200)),
                ('home', models.TextField()),
                ('preferred_study_locations', models.CharField(max_length=200)),
                ('Preferred_study_habits', models.CharField(max_length=200)),
                ('preferred_study_group_size', models.IntegerField()),
                ('weight_for_each_preference', models.CharField(max_length=200)),
            ],
        ),
    ]
