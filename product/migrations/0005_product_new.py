# Generated by Django 4.2.2 on 2023-07-13 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='new',
            field=models.CharField(choices=[('new', 'new')], default='', max_length=10),
            preserve_default=False,
        ),
    ]
