# Generated by Django 4.0.2 on 2022-05-31 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frkpapp', '0005_document_actors_signers_correspondents'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actors',
            name='id_doc',
        ),
        migrations.AddField(
            model_name='actors',
            name='document',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='frkpapp.document'),
        ),
    ]
