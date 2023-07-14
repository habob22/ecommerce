# Generated by Django 4.2.2 on 2023-07-13 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CATName', models.CharField(max_length=50)),
                ('CATDesc', models.TextField()),
                ('CATImg', models.ImageField(upload_to='category/')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='prodcut/')),
                ('prix', models.DecimalField(decimal_places=2, max_digits=5)),
                ('discountPrice', models.DecimalField(decimal_places=2, max_digits=5)),
                ('created', models.DateTimeField()),
            ],
        ),
    ]
