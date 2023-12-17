# Generated by Django 4.2.1 on 2023-12-16 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ec', '0015_rename_product_description_product_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='ARTIST',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=2000)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='artist',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ec.artist'),
            preserve_default=False,
        ),
    ]