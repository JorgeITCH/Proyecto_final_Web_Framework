# Generated by Django 3.1.2 on 2021-01-30 01:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20210126_2126'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=200)),
                ('max_number_questions', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='department',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='polls.department'),
            preserve_default=False,
        ),
    ]
