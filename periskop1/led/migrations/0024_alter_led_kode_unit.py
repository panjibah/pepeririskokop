# Generated by Django 3.2.7 on 2022-03-20 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('led', '0023_kasuslaporan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='led',
            name='kode_unit',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
