# Generated by Django 3.0.7 on 2021-02-06 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InstanceInfos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=63)),
                ('instanceId', models.IntegerField(unique=True)),
            ],
        ),
    ]
