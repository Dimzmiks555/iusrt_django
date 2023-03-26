# Generated by Django 4.1.7 on 2023-03-25 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("charges", "0002_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Document",
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
            ],
        ),
        migrations.AddField(
            model_name="packageofreceipts",
            name="documents",
            field=models.ManyToManyField(to="charges.document"),
        ),
        migrations.AddField(
            model_name="packageofservices",
            name="documents",
            field=models.ManyToManyField(to="charges.document"),
        ),
    ]
