# Generated by Django 4.1.7 on 2023-03-26 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "dictionary",
            "0007_alter_organization_options_alter_taxsystem_options_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="organization",
            name="tax_system",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="dictionary.taxsystem",
                verbose_name="Система налогообложения",
            ),
        ),
    ]