# Generated by Django 5.0.7 on 2024-08-05 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_book_author_delete_authorbook'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(blank=True, null=True, to='catalog.author'),
        ),
    ]
