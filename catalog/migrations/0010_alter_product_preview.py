# Generated by Django 4.2 on 2024-04-25 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_alter_version_is_current'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='preview',
            field=models.ImageField(upload_to='products/', verbose_name='Превью'),
        ),
    ]
