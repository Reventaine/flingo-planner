# Generated by Django 4.0.4 on 2022-05-24 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0005_remove_entry_uploader'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='image',
            field=models.ImageField(blank=True, default='01.jpeg', null=True, upload_to=''),
        ),
    ]
