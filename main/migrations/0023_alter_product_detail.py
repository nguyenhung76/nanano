# Generated by Django 3.2.8 on 2021-12-09 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_bannersmall'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='detail',
            field=models.CharField(max_length=600),
        ),
    ]
