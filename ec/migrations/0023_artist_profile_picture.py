# Generated by Django 4.2.1 on 2023-12-16 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ec', '0022_artist_profile_picture_category_regist_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='profile_picture',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]