# Generated by Django 3.1.7 on 2021-05-29 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('present2web', '0006_auto_20210529_0421'),
    ]

    operations = [
        migrations.AddField(
            model_name='tempurl',
            name='rules',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Правило вывода'),
        ),
    ]
