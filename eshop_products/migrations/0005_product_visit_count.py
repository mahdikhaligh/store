# Generated by Django 3.1.7 on 2021-03-03 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products', '0004_productgallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='visit_count',
            field=models.IntegerField(default=0),
        ),
    ]
