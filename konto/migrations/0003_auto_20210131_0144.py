# Generated by Django 3.1.3 on 2021-01-31 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('konto', '0002_auto_20210129_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='biography',
            field=models.TextField(blank=True, max_length=399, null=True, verbose_name='Bio'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='birthDate',
            field=models.DateField(blank=True, null=True, verbose_name='Birthday'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='countryOrigin',
            field=models.CharField(blank=True, max_length=99, null=True, verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='currentLocation',
            field=models.CharField(blank=True, max_length=99, null=True, verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profileAvatar',
            field=models.ImageField(blank=True, default='profilePhoto/default.jpg', upload_to='profilePhoto', verbose_name='Img'),
        ),
    ]