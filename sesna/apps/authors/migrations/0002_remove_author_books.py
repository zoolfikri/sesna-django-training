# Generated by Django 5.1.7 on 2025-03-16 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='books',
        ),
    ]
