# Generated by Django 5.0.6 on 2024-07-03 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=320)),
                ('sku', models.CharField(max_length=320, unique=True)),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('supplier_name', models.CharField(max_length=320)),
            ],
        ),
    ]
