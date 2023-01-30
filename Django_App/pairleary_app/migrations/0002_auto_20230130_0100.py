# Generated by Django 3.2.16 on 2023-01-29 16:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pairleary_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.IntegerField(primary_key=True, serialize=False)),
                ('order_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.DeleteModel(
            name='Content',
        ),
    ]
