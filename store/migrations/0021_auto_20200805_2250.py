# Generated by Django 2.0 on 2020-08-05 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0020_item_salt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='salt',
            field=models.CharField(max_length=200),
        ),
    ]
