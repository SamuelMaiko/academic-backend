# Generated by Django 5.0.2 on 2024-07-17 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_revisions', '0003_rename_is_open_revision_opened_by_reviewer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revisionmessage',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='revision_message_files'),
        ),
        migrations.AlterField(
            model_name='revisionmessage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='revision_message_images'),
        ),
    ]
