# Generated by Django 4.0.6 on 2022-10-21 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_remove_vote_value'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='review',
            unique_together=set(),
        ),
    ]
