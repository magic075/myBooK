# Generated by Django 3.1.3 on 2021-03-07 18:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0014_auto_20210213_2158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('biography', models.CharField(blank=True, max_length=80, null=True, verbose_name='O mnie')),
                ('profileAvatar', models.ImageField(blank=True, default='profilePhoto/default.jpg', upload_to='profilePhoto', verbose_name='Zdjęcie Profilowe')),
                ('birthDate', models.DateField(blank=True, null=True, verbose_name='Data urodzin')),
                ('city', models.CharField(blank=True, max_length=99, null=True, verbose_name='Miejscowość')),
                ('countryOrigin', django_countries.fields.CountryField(blank=True, max_length=2, null=True, verbose_name='Kraj pochodzenia')),
                ('github', models.URLField(blank=True, max_length=40, null=True)),
                ('snapchat', models.CharField(blank=True, max_length=40, null=True)),
                ('instagram', models.URLField(blank=True, max_length=40, null=True)),
                ('facebook', models.URLField(blank=True, max_length=40, null=True)),
                ('twitter', models.URLField(blank=True, max_length=40, null=True)),
                ('followers', models.ManyToManyField(blank=True, related_name='followers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
