# Generated by Django 4.1 on 2023-11-25 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0002_author_books_author_name_author_patronymic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]
