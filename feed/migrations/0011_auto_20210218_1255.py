# Generated by Django 3.1.3 on 2021-02-18 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0010_auto_20210214_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='postImages',
            field=models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d', verbose_name=''),
        ),
    ]