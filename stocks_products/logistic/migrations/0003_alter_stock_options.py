# Generated by Django 4.2.3 on 2023-07-21 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0002_alter_product_options_alter_stock_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stock',
            options={'ordering': ['id']},
        ),
    ]
