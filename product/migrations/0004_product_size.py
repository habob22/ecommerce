# Generated by Django 4.2.2 on 2023-07-13 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
