# Generated by Django 3.2.6 on 2022-06-08 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0032_customer_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='note',
            field=models.CharField(max_length=99999999999999999999, null=True),
        ),
    ]
