# Generated by Django 4.0.4 on 2022-05-16 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('qualification', models.CharField(max_length=250)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m%/d/')),
                ('facebook', models.URLField(max_length=100)),
                ('twitter', models.URLField(max_length=100)),
                ('instagram', models.URLField(max_length=100)),
                ('youtube', models.URLField(max_length=100)),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
