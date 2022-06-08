# Generated by Django 4.0.1 on 2022-05-11 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0003_alter_station_roomnr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='name',
            field=models.CharField(default='New', max_length=25),
        ),
        migrations.AlterField(
            model_name='station',
            name='url',
            field=models.CharField(max_length=45, unique=True),
        ),
    ]