# Generated by Django 3.2.7 on 2022-01-24 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('led', '0016_journal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessline',
            name='kode_bisnis',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='cabang',
            name='kode_cabang',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='cabang',
            name='segmentasi',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='cabang',
            name='status',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='cabang',
            name='tipe_cabang',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='coa',
            name='kode_coa',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='coa',
            name='nama',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='coa',
            name='status',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='kategorikejadian',
            name='kode_kategori1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='kategorikejadian',
            name='kode_kategori2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='kategorikejadian',
            name='kode_kategori3',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='led',
            name='dibuat_oleh',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='led',
            name='disetujui_oleh',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='led',
            name='ditemukan_oleh',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='led',
            name='mata_uang',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='led',
            name='nama_pembuat',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='led',
            name='nama_penemu',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='led',
            name='nomor_kasus',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='led',
            name='risiko_kredit',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='produk',
            name='kode_produk',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='unit',
            name='kode_unit',
            field=models.CharField(max_length=255),
        ),
    ]
