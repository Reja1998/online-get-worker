# Generated by Django 4.0.1 on 2022-10-07 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0010_remove_project_demo_link_remove_project_sourch_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='district',
        ),
        migrations.RemoveField(
            model_name='project',
            name='division',
        ),
        migrations.RemoveField(
            model_name='project',
            name='thana',
        ),
    ]
