# Generated by Django 5.0.3 on 2024-03-28 21:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Product category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Category',
                'db_table': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50, verbose_name='Product name')),
                ('product_description', models.TextField(verbose_name='Product description')),
                ('product_image', models.ImageField(upload_to='media/products', verbose_name='Product image')),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Product price')),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_fruits.categoryproduct', verbose_name='Product category')),
            ],
            options={
                'verbose_name': 'Products',
                'verbose_name_plural': 'Products',
                'db_table': 'Products',
            },
        ),
    ]