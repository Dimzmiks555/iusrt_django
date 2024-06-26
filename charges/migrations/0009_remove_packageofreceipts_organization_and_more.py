# Generated by Django 5.0.4 on 2024-04-09 06:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charges', '0008_alter_typeofreceipts_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='packageofreceipts',
            name='organization',
        ),
        migrations.RemoveField(
            model_name='packageofservices',
            name='organization',
        ),
        migrations.AddField(
            model_name='packageofreceipts',
            name='organization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='packageofservices',
            name='organization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
