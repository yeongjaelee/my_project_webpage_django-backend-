# Generated by Django 3.2.12 on 2023-02-15 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0007_board_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='board',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]