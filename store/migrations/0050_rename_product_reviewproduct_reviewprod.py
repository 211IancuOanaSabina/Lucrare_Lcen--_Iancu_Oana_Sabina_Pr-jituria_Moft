# Generated by Django 3.2.6 on 2022-06-14 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0049_reviewproduct_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviewproduct',
            old_name='product',
            new_name='reviewProd',
        ),
    ]
