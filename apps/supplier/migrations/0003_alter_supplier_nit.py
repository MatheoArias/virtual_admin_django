# Generated by Django 4.2.20 on 2025-05-07 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("supplier", "0002_alter_supplier_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="supplier",
            name="nit",
            field=models.CharField(max_length=20, unique=True, verbose_name="Nit"),
        ),
    ]
