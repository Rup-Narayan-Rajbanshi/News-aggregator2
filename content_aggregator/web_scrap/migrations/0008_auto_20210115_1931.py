# Generated by Django 3.1.5 on 2021-01-15 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_scrap', '0007_category_suscribe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='suscribe',
        ),
        migrations.RemoveField(
            model_name='category',
            name='user',
        ),
    ]