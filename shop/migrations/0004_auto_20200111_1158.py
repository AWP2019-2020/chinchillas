# Generated by Django 3.0.2 on 2020-01-11 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='created_by',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Category'),
        ),
        migrations.AddField(
            model_name='review',
            name='product',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='shop.Product'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=models.FileField(blank=True, null=True, upload_to='media/'),
        ),
    ]
