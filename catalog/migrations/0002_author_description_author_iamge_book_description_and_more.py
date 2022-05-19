# Generated by Django 4.0.4 on 2022-05-19 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='iamge',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]