# Generated by Django 3.2.7 on 2022-01-30 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('led', '0018_alter_produk_update_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='led',
            name='chk_kknled',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='led',
            name='chk_summ',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
