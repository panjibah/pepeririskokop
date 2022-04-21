# Generated by Django 3.2.7 on 2021-11-23 02:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('led', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='led',
            name='kode_unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='led.unit'),
        ),
        migrations.AddField(
            model_name='led',
            name='tipe_led',
            field=models.TextField(blank=True, null=True),
        ),
    ]
