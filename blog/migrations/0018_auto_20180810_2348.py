# Generated by Django 2.1 on 2018-08-10 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20180810_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='bannerURL',
            field=models.ImageField(upload_to='blog/static/blog/images/banner_url/'),
        ),
    ]