# Generated by Django 4.0.6 on 2022-10-23 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_remove_profile_bio'),
        ('notification', '0002_alter_notification_sender_alter_notification_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='text_preview',
        ),
        migrations.AlterField(
            model_name='notification',
            name='sender',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='send_noti', to='users.profile'),
        ),
    ]