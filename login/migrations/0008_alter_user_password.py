# Generated by Django 3.2.12 on 2023-01-12 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20230112_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]