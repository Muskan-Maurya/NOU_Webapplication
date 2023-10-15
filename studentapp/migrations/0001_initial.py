# Generated by Django 4.2.4 on 2023-10-04 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sturesponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollno', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('program', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=50)),
                ('year', models.CharField(max_length=10)),
                ('contactno', models.IntegerField()),
                ('emailaddress', models.CharField(max_length=50)),
                ('responsetype', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('responsetext', models.CharField(max_length=500)),
                ('responsedate', models.CharField(max_length=50)),
            ],
        ),
    ]
