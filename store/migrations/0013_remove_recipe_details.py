# Generated by Django 3.2.6 on 2022-06-02 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_auto_20220602_1528'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='details',
        ),
    ]
