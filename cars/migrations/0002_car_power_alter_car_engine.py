# Generated by Django 4.0.4 on 2022-06-05 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='power',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='car',
            name='engine',
            field=models.CharField(max_length=100),
        ),
    ]
