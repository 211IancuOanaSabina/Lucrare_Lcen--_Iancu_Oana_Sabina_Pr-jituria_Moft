# Generated by Django 3.2.6 on 2022-06-02 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_recipes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
