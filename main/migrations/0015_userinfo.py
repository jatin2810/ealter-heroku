# Generated by Django 3.0.6 on 2020-06-14 14:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0014_delete_userinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('user_info_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(blank=True, default='', max_length=254)),
                ('photo', models.ImageField(blank=True, upload_to='user_image')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
