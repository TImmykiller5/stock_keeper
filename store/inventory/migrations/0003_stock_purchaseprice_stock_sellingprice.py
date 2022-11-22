# Generated by Django 4.1.3 on 2022-11-21 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_remove_stock_category_remove_stock_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='PurchasePrice',
            field=models.DecimalField(decimal_places=2, max_digits=7, null=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='SellingPrice',
            field=models.DecimalField(decimal_places=2, max_digits=7, null=True),
        ),
    ]