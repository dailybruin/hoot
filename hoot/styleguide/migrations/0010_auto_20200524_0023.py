# Generated by Django 3.0.3 on 2020-05-24 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('styleguide', '0009_auto_20200218_1915'),
    ]

    operations = [
        migrations.RenameField(
            model_name='styleguideentry',
            old_name='section',
            new_name='sections',
        ),
    ]
