# Generated by Django 4.0.6 on 2022-10-20 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_remove_category_des'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='value',
            field=models.BooleanField(),
        ),
    ]
