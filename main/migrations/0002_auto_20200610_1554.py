# Generated by Django 3.0.6 on 2020-06-10 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='non_veg',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='veg',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='northindian',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='southindian',
            field=models.BooleanField(default=True),
        ),
    ]
