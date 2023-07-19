# Generated by Django 3.2.7 on 2021-09-23 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discount', '0006_auto_20210923_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='discount',
            name='condition',
            field=models.CharField(blank=True, choices=[('t', 'TIMELY'), ('f', 'FIRST_ORDER'), ('p', 'PERCENTAGE')], max_length=1, null=True),
        ),
    ]
