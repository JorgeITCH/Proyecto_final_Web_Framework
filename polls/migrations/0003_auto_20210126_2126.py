# Generated by Django 3.1.2 on 2021-01-27 02:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_choiceusernames'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choiceusernames',
            old_name='username',
            new_name='usernamed',
        ),
    ]
