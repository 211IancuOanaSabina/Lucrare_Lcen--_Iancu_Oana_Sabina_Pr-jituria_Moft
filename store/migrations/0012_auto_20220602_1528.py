# Generated by Django 3.2.6 on 2022-06-02 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_remove_recipe_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='cake',
            new_name='cakeIng',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='cream',
            new_name='cakePrep',
        ),
        migrations.AddField(
            model_name='recipe',
            name='creamIng',
            field=models.CharField(max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='creamPrep',
            field=models.CharField(max_length=5000, null=True),
        ),
    ]