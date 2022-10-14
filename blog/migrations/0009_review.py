# Generated by Django 4.0.6 on 2022-08-29 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_blog_category_blog_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(blank=True, null=True)),
                ('value', models.CharField(choices=[('up', 'up vote'), ('down', 'down vote')], max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blogreview', to='blog.blog')),
            ],
        ),
    ]
