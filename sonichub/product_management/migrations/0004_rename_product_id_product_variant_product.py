# Generated by Django 5.0 on 2023-12-23 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_management', '0003_rename_product_id_product_images_product_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product_variant',
            old_name='product_id',
            new_name='product',
        ),
    ]
