# Generated by Django 4.2.6 on 2023-10-31 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_comment_content_alter_comment_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
    ]
