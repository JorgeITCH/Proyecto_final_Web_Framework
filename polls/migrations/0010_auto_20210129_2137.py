# Generated by Django 3.1.2 on 2021-01-30 02:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_delete_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choiceusernames',
            name='choice',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='ChoiceUsernames',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
