# Generated by Django 3.2.3 on 2021-05-24 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profiledetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiledetails',
            name='covid',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profiledetails',
            name='occupation',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
