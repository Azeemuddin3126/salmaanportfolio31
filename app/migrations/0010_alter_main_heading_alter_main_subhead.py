# Generated by Django 4.1.1 on 2022-10-03 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_main_img1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='heading',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='main',
            name='subhead',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
