# Generated by Django 4.1 on 2022-08-11 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('phone_no', models.BigIntegerField()),
                ('dob', models.DateField()),
                ('email', models.CharField(max_length=100)),
                ('product', models.CharField(max_length=100)),
            ],
        ),
    ]
