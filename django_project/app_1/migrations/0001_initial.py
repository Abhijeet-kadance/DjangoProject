# Generated by Django 4.1.1 on 2022-09-18 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trainers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trainer_name', models.CharField(max_length=200)),
                ('trainer_age', models.PositiveIntegerField(blank=True, null=True)),
                ('trainer_type', models.CharField(max_length=200)),
            ],
        ),
    ]