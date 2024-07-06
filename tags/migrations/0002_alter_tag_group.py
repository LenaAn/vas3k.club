# Generated by Django 3.2.13 on 2024-07-06 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='group',
            field=models.CharField(choices=[('personal', 'Я'), ('where', 'Где я'), ('club', 'Для других членов Клуба я...'), ('hobbies', 'Хобби'), ('collectible', 'Коллекционные теги'), ('other', 'Другие')], default='other', max_length=32),
        ),
    ]
