# Generated by Django 2.1 on 2018-08-10 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20180810_1614'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.AddField(
            model_name='post',
            name='liked',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ComputerIP',
        ),
    ]