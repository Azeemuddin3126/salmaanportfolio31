# Generated by Django 4.1.1 on 2022-09-30 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_project_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='image1',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='project',
            name='image2',
        ),
    ]
