# Generated by Django 4.0.1 on 2022-02-05 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0004_alter_seller_address_alter_seller_market_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='market',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]