# Generated by Django 3.2.23 on 2024-08-05 11:01

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_app', '0002_auto_20240719_0829'),
        ('auth_app', '0005_alter_user_password'),
        ('cart_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('comment', models.TextField(blank=True, default='', null=True, verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения')),
                ('qnt', models.DecimalField(blank=True, decimal_places=3, default=1, max_digits=15, null=True, verbose_name='Количество')),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog_app.good', verbose_name='Товар')),
                ('token', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_app.token', verbose_name='Токен')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
