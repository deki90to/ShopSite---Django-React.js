# Generated by Django 3.1.2 on 2021-02-06 12:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(help_text='Product name', max_length=255)),
            ],
            options={
                'ordering': ['brand_name'],
            },
        ),
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField(max_length=100)),
                ('note', models.TextField(blank=True, max_length=300, null=True)),
                ('date_buyed', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date_buyed'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(help_text='Category name', max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ['category_name'],
            },
        ),
        migrations.CreateModel(
            name='ProductName',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=200)),
                ('product_description', models.TextField(max_length=500)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('product_picture', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=100, size=[200, 110], upload_to='pictures')),
                ('product_price', models.IntegerField(default='0', null=True)),
                ('buyer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='buyer', to='shop_app.buyer')),
                ('product_brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop_app.brand')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_posted'],
            },
        ),
        migrations.AddField(
            model_name='buyer',
            name='buyed_item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='buyed_item', to='shop_app.productname'),
        ),
        migrations.AddField(
            model_name='brand',
            name='brand_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_category', to='shop_app.category'),
        ),
    ]
