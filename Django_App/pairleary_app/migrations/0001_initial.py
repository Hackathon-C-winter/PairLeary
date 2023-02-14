# Generated by Django 3.2.16 on 2023-02-14 13:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='ユーザー名')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='メールアドレス')),
                ('gender_type', models.CharField(blank=True, max_length=15, null=True, verbose_name='性別')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_date', models.DateField(help_text='予約日付')),
                ('order_time_range_type', models.CharField(default='null', max_length=10)),
                ('category', models.CharField(default='null', max_length=150)),
                ('hope_gender_type', models.CharField(blank=True, default=None, max_length=15, null=True, verbose_name='性別')),
                ('comment', models.CharField(default='null', max_length=255)),
                ('matched_user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='matched_user_id', to=settings.AUTH_USER_MODEL)),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
