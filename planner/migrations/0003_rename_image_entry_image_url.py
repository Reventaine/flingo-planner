# Generated by Django 4.0.4 on 2022-05-24 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0002_entry_uploader'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='image',
            new_name='image_url',
        ),
    ]
