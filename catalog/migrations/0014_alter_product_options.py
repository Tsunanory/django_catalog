# Generated by Django 4.2.7 on 2024-05-08 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_alter_product_options_product_is_published'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'permissions': [('set_published', 'Can publish post'), ('Change description', 'Can change description')], 'verbose_name': 'продукт', 'verbose_name_plural': 'продукты'},
        ),
    ]
