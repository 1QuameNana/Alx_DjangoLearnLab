# Generated by Django 5.1 on 2024-08-17 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='Publication_year',
            new_name='publication_year',
        ),
    ]
