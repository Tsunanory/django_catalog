# Generated by Django 4.2 on 2024-04-24 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='is_current',
            field=models.BooleanField(default=False),
        ),
    ]