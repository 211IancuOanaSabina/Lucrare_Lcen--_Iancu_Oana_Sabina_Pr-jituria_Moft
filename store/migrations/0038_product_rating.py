# Generated by Django 3.2.6 on 2022-06-13 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0037_auto_20220613_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=2),
        ),
    ]
