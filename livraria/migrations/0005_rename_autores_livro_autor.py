# Generated by Django 4.2.2 on 2023-06-05 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livraria', '0004_rename_tirulo_livro_titulo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='livro',
            old_name='autores',
            new_name='autor',
        ),
    ]