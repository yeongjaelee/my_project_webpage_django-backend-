# Generated by Django 3.2.12 on 2023-02-06 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0005_board_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files'),
        ),
    ]
