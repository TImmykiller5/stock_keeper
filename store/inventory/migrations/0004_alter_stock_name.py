# Generated by Django 4.1.3 on 2022-11-22 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_stock_purchaseprice_stock_sellingprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]