# Generated by Django 2.1 on 2018-08-08 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('content', models.TextField()),
                ('reply_id', models.IntegerField(max_length=99999)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('author', models.CharField(max_length=15)),
                ('date', models.DateTimeField()),
                ('banner_url', models.ImageField(upload_to='blog/static/blog/images/banner_url')),
                ('categories', models.CharField(max_length=60)),
                ('header', models.CharField(max_length=300)),
                ('content', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post'),
        ),
    ]