# Generated by Django 3.2.8 on 2021-12-08 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20210709_2210'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bannersmall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='banner_imgs/')),
                ('alt_text', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name_plural': 'Bannersmall',
            },
        ),
    ]
