# Generated by Django 5.0.4 on 2024-04-09 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0009_alter_document_options_alter_document_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='title',
            field=models.CharField(blank=True, max_length=255, verbose_name='Наименование организации без ОПФ'),
        ),
    ]
