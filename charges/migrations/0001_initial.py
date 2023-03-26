# Generated by Django 4.1.7 on 2023-03-25 11:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PackageOfReceipts",
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
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Оплачено", "Оплачено"),
                            ("Требуется оплата", "Требуется оплата"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "created_at",
                    models.DateField(
                        default=django.utils.timezone.now, verbose_name="Дата создания"
                    ),
                ),
                (
                    "must_be_payed_at",
                    models.DateField(
                        default=django.utils.timezone.now,
                        verbose_name="Должно быть оплачено до",
                    ),
                ),
                (
                    "summ",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Сумма"
                    ),
                ),
                ("description", models.TextField(verbose_name="Комментарий")),
            ],
        ),
        migrations.CreateModel(
            name="PackageOfServices",
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
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Оплачено", "Оплачено"),
                            ("Требуется оплата", "Требуется оплата"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "created_at",
                    models.DateField(
                        default=django.utils.timezone.now, verbose_name="Дата создания"
                    ),
                ),
                (
                    "must_be_payed_at",
                    models.DateField(
                        default=django.utils.timezone.now,
                        verbose_name="Должно быть оплачено до",
                    ),
                ),
                (
                    "summ",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Сумма"
                    ),
                ),
                ("description", models.TextField(verbose_name="Комментарий")),
            ],
        ),
        migrations.CreateModel(
            name="Type",
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
                (
                    "name",
                    models.CharField(max_length=100, verbose_name="Наименование типа"),
                ),
            ],
        ),
    ]