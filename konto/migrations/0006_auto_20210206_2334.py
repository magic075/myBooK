# Generated by Django 3.1.3 on 2021-02-06 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('konto', '0005_auto_20210206_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='facebook',
            field=models.URLField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='github',
            field=models.URLField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='instagram',
            field=models.URLField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='twitter',
            field=models.URLField(blank=True, max_length=40, null=True),
        ),
    ]
