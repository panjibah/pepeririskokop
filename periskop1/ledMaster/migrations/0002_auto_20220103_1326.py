# Generated by Django 3.2.7 on 2022-01-03 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledMaster', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ledhistoris',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='ledhistoris',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
