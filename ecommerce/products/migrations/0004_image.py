# Generated by Django 3.0.6 on 2020-05-14 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200514_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products/images/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
        ),
    ]
