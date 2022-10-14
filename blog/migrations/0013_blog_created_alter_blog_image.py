# Generated by Django 4.0.6 on 2022-08-30 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_blog_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, default='blog/default.jpg', null=True, upload_to='Blog'),
        ),
    ]
