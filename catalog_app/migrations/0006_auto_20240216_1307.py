# Generated by Django 3.2.23 on 2024-02-16 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_app', '0005_remove_good_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='name',
            field=models.CharField(blank=True, db_index=True, default='', max_length=150, null=True, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='name',
            field=models.CharField(blank=True, db_index=True, default='', max_length=150, null=True, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='pricekind',
            name='name',
            field=models.CharField(blank=True, db_index=True, default='', max_length=150, null=True, verbose_name='Наименование'),
        ),
    ]
