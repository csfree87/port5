# Generated by Django 3.2 on 2022-07-07 00:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact_form',
            new_name='Contact',
        ),
    ]