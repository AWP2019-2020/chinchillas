# Generated by Django 3.0.2 on 2020-01-11 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingcart',
            name='state',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
