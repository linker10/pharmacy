# Generated by Django 3.0.6 on 2020-06-01 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_orderitem_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.SlugField(default='test-product'),
            preserve_default=False,
        ),
    ]