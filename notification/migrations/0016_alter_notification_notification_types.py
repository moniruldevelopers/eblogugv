# Generated by Django 4.2.7 on 2023-12-06 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0015_alter_notification_notification_types'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notification_types',
            field=models.CharField(choices=[('Blog', 'Blog'), ('Follow', 'Follow'), ('Like', 'Like')], max_length=20),
        ),
    ]
