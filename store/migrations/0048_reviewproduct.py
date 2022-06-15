# Generated by Django 3.2.6 on 2022-06-14 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0047_auto_20220614_1812'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('revtitle', models.CharField(max_length=300, null=True)),
                ('revmess', models.CharField(max_length=500, null=True)),
                ('rating', models.DecimalField(decimal_places=2, default=0.0, max_digits=2)),
            ],
        ),
    ]
