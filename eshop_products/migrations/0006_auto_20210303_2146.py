# Generated by Django 3.1.7 on 2021-03-03 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products', '0005_product_visit_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='visit_count',
            field=models.IntegerField(default=' '),
        ),
    ]
