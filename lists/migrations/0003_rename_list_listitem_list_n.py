# Generated by Django 3.2.7 on 2023-09-26 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_auto_20230924_0359'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listitem',
            old_name='list',
            new_name='list_n',
        ),
    ]
