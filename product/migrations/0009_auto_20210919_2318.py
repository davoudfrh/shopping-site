# Generated by Django 3.2.7 on 2021-09-19 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20210919_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='en_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='brand',
            name='fa_name',
            field=models.CharField(max_length=200),
        ),
    ]
