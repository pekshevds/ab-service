# Generated by Django 3.2.23 on 2024-07-10 06:15

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('image_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения')),
                ('name', models.CharField(blank=True, db_index=True, default='', max_length=150, null=True, verbose_name='Наименование')),
                ('is_group', models.BooleanField(default=False, verbose_name='Это группа')),
                ('count', models.IntegerField(blank=True, default=0, null=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='childs', to='catalog_app.category', verbose_name='Родитель')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения')),
                ('name', models.CharField(blank=True, db_index=True, default='', max_length=150, null=True, verbose_name='Наименование')),
                ('is_group', models.BooleanField(default=False, verbose_name='Это группа')),
                ('art', models.CharField(blank=True, db_index=True, default='', max_length=50, null=True, verbose_name='Артикул')),
                ('code', models.CharField(blank=True, default='', max_length=11, null=True, verbose_name='Код')),
                ('balance', models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=15, null=True, verbose_name='Остаток')),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True, verbose_name='Цена')),
                ('slug', models.SlugField(blank=True, max_length=250, null=True, unique=True)),
                ('is_active', models.BooleanField(default=False, verbose_name='Активен')),
                ('description', models.CharField(blank=True, default='', max_length=1024, null=True, verbose_name='Описание')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='goods', to='catalog_app.category', verbose_name='Категория')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='image_app.image', verbose_name='Изображение (превью)')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения')),
                ('name', models.CharField(blank=True, db_index=True, default='', max_length=150, null=True, verbose_name='Наименование')),
                ('is_group', models.BooleanField(default=False, verbose_name='Это группа')),
                ('count', models.IntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'verbose_name': 'Производитель',
                'verbose_name_plural': 'Производители',
            },
        ),
        migrations.CreateModel(
            name='GoodsImage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения')),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='images', to='catalog_app.good', verbose_name='Номенклатура')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='image_app.image', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения товара',
            },
        ),
        migrations.AddField(
            model_name='good',
            name='manufacturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='goods', to='catalog_app.manufacturer', verbose_name='Производитель'),
        ),
    ]
