# Generated by Django 3.1.7 on 2021-05-30 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('present2web', '0007_tempurl_rules'),
    ]

    operations = [
        migrations.AlterField(
            model_name='present',
            name='image',
            field=models.TextField(blank=True, null=True, verbose_name='Ссылка на изображение'),
        ),
        migrations.AlterField(
            model_name='present',
            name='url',
            field=models.TextField(verbose_name='Ссылка на подарок'),
        ),
    ]
