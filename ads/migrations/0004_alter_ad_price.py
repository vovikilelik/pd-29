# Generated by Django 4.0.6 on 2022-07-11 17:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_alter_ad_is_published_alter_ad_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='price',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(limit_value=0)]),
        ),
    ]
