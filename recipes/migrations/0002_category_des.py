# Generated by Django 4.0.6 on 2022-10-18 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='des',
            field=models.TextField(null=True),
        ),
    ]
