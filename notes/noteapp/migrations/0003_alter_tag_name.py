# Generated by Django 4.2.1 on 2023-06-09 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noteapp', '0002_note_user_tag_user_alter_tag_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]
