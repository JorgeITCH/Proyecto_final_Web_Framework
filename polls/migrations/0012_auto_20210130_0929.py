# Generated by Django 3.1.2 on 2021-01-30 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_auto_20210129_2139'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='department',
            new_name='department_text',
        ),
    ]