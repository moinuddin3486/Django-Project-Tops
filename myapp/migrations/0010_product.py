# Generated by Django 5.0.4 on 2024-04-30 11:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_category', models.CharField(choices=[('Men', 'Men'), ('Women', 'Women'), ('Kids', 'Kids')], max_length=100)),
                ('product_name', models.CharField(max_length=100)),
                ('product_desc', models.TextField()),
                ('product_price', models.PositiveIntegerField()),
                ('product_picture', models.ImageField(upload_to='Product_picture/')),
                ('product_size', models.CharField(choices=[('s', 's'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XLL', 'XLL')], max_length=100)),
                ('product_color', models.CharField(choices=[('Red', 'Red'), ('White', 'White'), ('Yellow', 'Yellow'), ('Black', 'Black')], max_length=100)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
    ]
