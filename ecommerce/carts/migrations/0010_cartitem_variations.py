# Generated by Django 2.2.6 on 2020-05-17 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_delete_variationmanager'),
        ('carts', '0009_auto_20200516_0557'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='variations',
            field=models.ManyToManyField(blank=True, null=True, to='products.Variation'),
        ),
    ]
