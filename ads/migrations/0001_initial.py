# Generated by Django 4.0.6 on 2022-07-08 00:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.TextField(validators=[django.core.validators.MinLengthValidator(10)])),
                ('price', models.FloatField()),
                ('description', models.TextField(null=True)),
                ('is_published', models.BooleanField()),
                ('image', models.ImageField(null=True, upload_to='images/')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
                'ordering': ['-price'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('slug', models.SlugField(max_length=10, unique=True, validators=[django.core.validators.MinLengthValidator(5)])),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
    ]
