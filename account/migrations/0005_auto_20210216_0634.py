# Generated by Django 3.1.2 on 2021-02-16 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20210213_0053'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='verified',
            field=models.CharField(default='0', max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='verified_code',
            field=models.CharField(default='', max_length=6, null=True),
        ),
    ]
