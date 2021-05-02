# Generated by Django 3.1.7 on 2021-04-29 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_remove_contact_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='desc',
            new_name='suggestion',
        ),
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=122, null=True),
        ),
    ]
