# Generated by Django 4.0.2 on 2022-05-31 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frkpapp', '0006_remove_actors_id_doc_actors_document'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Actors',
            new_name='Performers',
        ),
        migrations.AlterModelTable(
            name='performers',
            table='performers',
        ),
    ]