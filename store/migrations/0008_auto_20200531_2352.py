# Generated by Django 3.0.6 on 2020-05-31 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_item_discount_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='discount_price',
            new_name='old_price',
        ),
    ]
