# Generated by Django 4.2.4 on 2023-11-21 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0002_categories_products_remove_order_products_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
