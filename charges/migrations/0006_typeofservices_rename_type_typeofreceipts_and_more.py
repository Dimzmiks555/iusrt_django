# Generated by Django 4.1.7 on 2023-08-27 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("charges", "0005_documentofpackageofreceipts_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="TypeOfServices",
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
            options={
                "verbose_name": "Тип",
                "verbose_name_plural": "Тип",
            },
        ),
        migrations.RenameModel(
            old_name="Type",
            new_name="TypeOfReceipts",
        ),
        migrations.AlterField(
            model_name="packageofservices",
            name="type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="charges.typeofservices"
            ),
        ),
    ]
