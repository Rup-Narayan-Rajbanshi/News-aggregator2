# Generated by Django 3.1.5 on 2021-01-14 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_scrap', '0004_data_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='image',
        ),
        migrations.AddField(
            model_name='data',
            name='image_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
