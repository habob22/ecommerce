# Generated by Django 4.2.2 on 2023-07-13 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_alter_product_created_futurproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='futurproduct',
            name='category',
            field=models.CharField(max_length=30),
        ),
    ]
