# Generated by Django 4.0 on 2022-08-30 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_remove_product_customer_alter_product_statut'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='objetdeal',
            name='code',
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
    ]
