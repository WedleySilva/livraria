# Generated by Django 4.2.2 on 2023-06-06 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livraria', '0006_rename_autor_livro_autores'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livro',
            name='categoria',
        ),
        migrations.AddField(
            model_name='livro',
            name='categoria',
            field=models.ManyToManyField(related_name='livros', to='livraria.categoria'),
        ),
    ]
