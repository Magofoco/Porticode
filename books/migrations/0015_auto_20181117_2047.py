# Generated by Django 2.1.3 on 2018-11-17 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0014_auto_20181117_2037'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='user',
            new_name='original_poster',
        ),
    ]