# Generated by Django 3.1.7 on 2021-04-29 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20210421_1029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='name',
        ),
    ]
