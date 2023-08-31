# Generated by Django 4.1.7 on 2023-08-30 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("charges", "0006_typeofservices_rename_type_typeofreceipts_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="PaymentOfPackageOfServices",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("file", models.FileField(upload_to="", verbose_name="Файл")),
                (
                    "package_of_services",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="charges.packageofservices",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PaymentOfPackageOfReceipts",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("file", models.FileField(upload_to="", verbose_name="Файл")),
                (
                    "package_of_receipts",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="charges.packageofreceipts",
                    ),
                ),
            ],
        ),
    ]
