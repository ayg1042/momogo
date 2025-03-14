# Generated by Django 5.1.1 on 2024-11-24 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bapgo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('category', models.CharField(max_length=20)),
                ('rate', models.IntegerField(default=0)),
                ('rcount', models.IntegerField(default=0)),
                ('status', models.CharField(max_length=15)),
                ('purl', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rdate', models.DateField()),
                ('rrate', models.IntegerField(default=0)),
                ('rtext', models.TextField()),
            ],
        ),
    ]
