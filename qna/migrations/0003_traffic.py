# Generated by Django 3.2.12 on 2023-01-04 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0002_alter_reply_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Traffic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
