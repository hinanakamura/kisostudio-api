# Generated by Django 4.2.1 on 2023-08-27 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ec', '0011_alter_account_first_name_alter_account_last_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]