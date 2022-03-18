# Generated by Django 3.1.7 on 2021-02-28 20:10

from django.db import migrations, models
import django.db.models.deletion
import eshop_products.models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products', '0003_product_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to=eshop_products.models.upload_image_gallery_path)),
                ('active', models.BooleanField(default=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eshop_products.product')),
            ],
        ),
    ]
