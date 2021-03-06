# Generated by Django 3.2.6 on 2022-06-13 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0036_product_digital'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredients', models.CharField(max_length=5000, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='digital',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
