# Generated by Django 5.0.6 on 2024-06-03 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('subject', models.CharField(max_length=150)),
                ('address', models.TextField()),
            ],
        ),
    ]
