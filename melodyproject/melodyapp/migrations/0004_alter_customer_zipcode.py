# Generated by Django 5.0.6 on 2024-05-17 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('melodyapp', '0003_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='zipcode',
            field=models.IntegerField(default=0),
        ),
    ]
