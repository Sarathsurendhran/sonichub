# Generated by Django 5.0 on 2023-12-25 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_management', '0004_rename_product_id_product_variant_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='images',
            field=models.ImageField(default='C:\\Users\\sarat\\Documents\\ noimage.jpg', upload_to='product_images'),
        ),
        migrations.DeleteModel(
            name='Product_images',
        ),
    ]
