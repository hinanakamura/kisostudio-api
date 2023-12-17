# Generated by Django 4.2.1 on 2023-12-16 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ec', '0021_artist_profile_picture_link_site_link_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='regist_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='gallery',
            name='regist_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='regist_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='link',
            name='site',
            field=models.CharField(choices=[('X', 'X'), ('instagram', 'Instagram'), ('web', 'Web')], max_length=15),
        ),
    ]