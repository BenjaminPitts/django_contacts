# Generated by Django 3.2 on 2021-04-10 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='album1',
            field=models.CharField(default='e', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='album2',
            field=models.CharField(default='e', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='bio',
            field=models.TextField(default='e'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='image1',
            field=models.CharField(default='e', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='image2',
            field=models.CharField(default='e', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='link',
            field=models.CharField(default='e', max_length=200),
            preserve_default=False,
        ),
    ]
