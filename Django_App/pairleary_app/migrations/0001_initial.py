# Generated by Django 3.2.16 on 2023-01-27 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('condition_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(default='null', max_length=255)),
                ('category', models.CharField(default='null', max_length=255)),
                ('comment', models.CharField(default='null', max_length=255)),
            ],
        ),
    ]
