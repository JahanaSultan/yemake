# Generated by Django 4.0.6 on 2022-10-18 20:08

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0018_alter_blog_isactive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='Açıqlama'),
        ),
        migrations.AlterField(
            model_name='review',
            name='body',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
