# Generated by Django 3.1.7 on 2021-03-03 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='ref_id',
            field=models.CharField(default=0, max_length=100),
        ),
    ]