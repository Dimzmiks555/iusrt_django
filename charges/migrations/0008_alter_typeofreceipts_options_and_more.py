# Generated by Django 5.0.4 on 2024-04-09 06:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charges', '0007_paymentofpackageofservices_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='typeofreceipts',
            options={'verbose_name': 'Тип квитанций', 'verbose_name_plural': 'Типы квитанций'},
        ),
        migrations.AlterModelOptions(
            name='typeofservices',
            options={'verbose_name': 'Тип услуг', 'verbose_name_plural': 'Типы услуг'},
        ),
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
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='packageofservices',
            name='organization',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
