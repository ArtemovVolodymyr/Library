# Generated by Django 4.1 on 2023-07-06 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_customuser_created_at_customuser_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.IntegerField(choices=[(0, 'visitor'), (1, 'librarian')], default=0),
        ),
    ]
