# Generated by Django 3.2.6 on 2022-06-02 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_remove_recipe_pictures'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Recipe',
        ),
    ]
