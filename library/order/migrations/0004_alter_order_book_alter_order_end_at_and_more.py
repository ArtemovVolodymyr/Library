# Generated by Django 4.1 on 2023-07-18 14:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_book_count_book_description_book_name_alter_book_id'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0003_alter_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='book.book'),
        ),
        migrations.AlterField(
            model_name='order',
            name='end_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='plated_end_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
