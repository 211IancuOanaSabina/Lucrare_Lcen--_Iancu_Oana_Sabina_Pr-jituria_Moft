# Generated by Django 3.2.6 on 2022-06-14 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0040_delete_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='revmess',
            field=models.CharField(choices=[('lactoza', 'lactoza'), ('gluten', 'gluten')], max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='revtitle',
            field=models.CharField(choices=[('lactoza', 'lactoza'), ('gluten', 'gluten')], max_length=300, null=True),
        ),
    ]
