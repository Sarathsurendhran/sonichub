# Generated by Django 5.0 on 2023-12-25 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_management', '0008_alter_product_images_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_images',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='thumbnail_images'),
        ),
    ]