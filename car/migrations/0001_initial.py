# Generated by Django 3.0.3 on 2020-02-15 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='car_images')),
                ('description', models.TextField()),
                ('daily_rent', models.IntegerField()),
                ('hire_on', models.DateField()),
                ('return_on', models.DateField()),
                ('type', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('is_available', models.BooleanField()),
            ],
        ),
    ]
