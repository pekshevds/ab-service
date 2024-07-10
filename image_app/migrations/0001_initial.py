# Generated by Django 3.2.23 on 2024-07-10 06:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения')),
                ('name', models.CharField(blank=True, db_index=True, default='', max_length=150, null=True, verbose_name='Наименование')),
                ('is_group', models.BooleanField(default=False, verbose_name='Это группа')),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='images/', verbose_name='Файл изображения')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
    ]
