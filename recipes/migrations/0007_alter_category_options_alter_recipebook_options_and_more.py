# Generated by Django 4.0.6 on 2022-10-23 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_alter_review_unique_together'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Kateqoriya', 'verbose_name_plural': 'Kateqoriyalar'},
        ),
        migrations.AlterModelOptions(
            name='recipebook',
            options={'verbose_name': 'Resept Dəftəri', 'verbose_name_plural': 'Resept Dəftəri'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-created'], 'verbose_name': 'Şərh', 'verbose_name_plural': 'Şərhlər'},
        ),
        migrations.AlterModelOptions(
            name='vote',
            options={'verbose_name': 'Bəyənmə', 'verbose_name_plural': 'Bəyənmələr'},
        ),
    ]
