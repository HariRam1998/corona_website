# Generated by Django 3.2.3 on 2021-05-24 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='profiledetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usermail', models.CharField(max_length=50)),
                ('tagline', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('phoneno', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('region', models.CharField(max_length=20)),
                ('proimage', models.TextField()),
            ],
        ),
    ]
