# Generated by Django 2.0 on 2020-08-05 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_auto_20200805_2244'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='salt',
            field=models.FloatField(default=0),
        ),
    ]
