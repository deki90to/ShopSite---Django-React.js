# Generated by Django 3.1.2 on 2021-02-12 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0004_remove_productname_mult_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productname',
            name='product_picture',
            field=models.FileField(null=True, upload_to='pictures'),
        ),
    ]
