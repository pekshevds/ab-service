# Generated by Django 3.2.23 on 2024-07-01 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0012_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$260000$VCjN0I3QfKZRKfwCgkkeDm$Kdaz8dycln+wfkDi6F0Rqmq7GmL/9X03eDx5v2Rl1G0=', max_length=128, verbose_name='password'),
        ),
    ]
