# Generated by Django 4.0.6 on 2022-10-19 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_category_des'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='des',
        ),
    ]
