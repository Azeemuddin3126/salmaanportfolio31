# Generated by Django 4.1.1 on 2022-10-03 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_main_heading'),
    ]

    operations = [
        migrations.CreateModel(
            name='education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=225)),
                ('course', models.CharField(max_length=225)),
                ('university', models.CharField(max_length=225)),
                ('passout', models.IntegerField()),
                ('cgpa', models.IntegerField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=225)),
                ('company', models.CharField(max_length=225)),
                ('duration', models.CharField(max_length=225)),
                ('disc', models.TextField(blank=True, max_length=2223, null=True)),
                ('skills', models.CharField(max_length=223)),
            ],
        ),
        migrations.DeleteModel(
            name='about',
        ),
    ]
