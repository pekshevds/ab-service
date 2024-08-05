# Generated by Django 3.2.23 on 2024-08-05 10:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0003_alter_user_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('comment', models.TextField(blank=True, default='', null=True, verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения')),
                ('name', models.CharField(blank=True, db_index=True, default='', max_length=150, null=True, verbose_name='Наименование')),
                ('is_group', models.BooleanField(default=False, verbose_name='Это группа')),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$260000$tdzS3Z7f0irTUi6H7ANZh5$DSVVB/9Yjco1mDJcyVL1ly/dxtmt1XQxCD+BKM4LnzE=', max_length=128, verbose_name='password'),
        ),
    ]
