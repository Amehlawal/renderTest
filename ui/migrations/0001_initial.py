# Generated by Django 5.2 on 2025-04-11 15:36

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('slug', models.SlugField()),
                ('category', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ui.category')),
            ],
        ),
        migrations.CreateModel(
            name='SubSubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('slug', models.SlugField()),
                ('subcategory', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ui.subcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('shippingFrom', models.CharField()),
                ('availability', models.CharField()),
                ('condition', models.CharField()),
                ('views', models.PositiveIntegerField(default=0)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('slug', models.SlugField()),
                ('brand', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ui.brand')),
                ('model', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ui.model')),
                ('subsubcategory', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ui.subsubcategory')),
            ],
        ),
    ]
