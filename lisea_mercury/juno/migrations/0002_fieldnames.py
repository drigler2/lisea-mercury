# Generated by Django 3.0.7 on 2021-02-06 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juno', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FieldNames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=63)),
                ('password', models.CharField(max_length=63)),
                ('uniqueId', models.CharField(max_length=63)),
                ('enabled', models.CharField(max_length=63)),
                ('authorityName', models.CharField(max_length=63)),
            ],
        ),
    ]