# Generated by Django 3.2.6 on 2022-06-14 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0044_auto_20220614_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='alergens',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='revmess',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='revtitle',
            field=models.CharField(max_length=300, null=True),
        ),
    ]