# Generated by Django 4.1.1 on 2022-10-03 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_about_contact_home_projects_delete_project'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='home',
            new_name='main',
        ),
    ]
