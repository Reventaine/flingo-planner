# Generated by Django 4.0.4 on 2022-05-18 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0004_entry_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='text',
            field=models.TextField(default=None, null=True),
        ),
    ]
