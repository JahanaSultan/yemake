# Generated by Django 4.0.6 on 2022-10-18 20:52

from django.db import migrations
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_alter_blog_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=django_quill.fields.QuillField(),
        ),
    ]
