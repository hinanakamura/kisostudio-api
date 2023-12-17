# Generated by Django 4.2.1 on 2023-12-16 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ec', '0023_artist_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='regist_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='regist_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='regist_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='regist_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='link',
            name='regist_date',
            field=models.DateTimeField(null=True),
        ),
    ]