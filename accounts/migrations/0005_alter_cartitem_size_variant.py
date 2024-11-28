# Generated by Django 5.0.6 on 2024-06-24 07:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_cartitem_size_variant'),
        ('products', '0005_alter_coupon_discount_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='size_variant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.sizevariant'),
        ),
    ]