# Generated by Django 2.1.7 on 2019-03-03 20:00

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_post_view_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(default='test'),
            preserve_default=False,
        ),
    ]
