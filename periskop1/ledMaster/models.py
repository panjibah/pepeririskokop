from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateField
from django.db.models.fields.related import ForeignKey
from softdelete.models import SoftDeleteObject



class LedHistoris(models.Model):
    laporan_id = models.IntegerField(default=None,blank=True,null=True)
    nomor_kasus             = models.CharField(max_length =50,default=None,blank=True,null=True)
    historis_id = models.IntegerField(default=None,blank=True,null=True)
    tanggal_kejadian        = models.DateField(default=None,blank=True,null=True)
    tanggal_teridentifikasi = models.DateField(default=None,blank=True,null=True)
    tanggal_input           = models.DateField(default=None,blank=True,null=True)
    tanggal_selesai         = models.DateField(default=None,blank=True,null=True)
    tanggal_update          = models.DateTimeField(default=None,blank=True,null=True)
    jumlah_kasus            = models.IntegerField(default=None,blank=True,null=True)
    nama_pembuat            = models.CharField(max_length=100,default=None,blank=True,null=True)
    status                  = models.CharField(max_length=250,default=None,blank=True,null=True)
    kode_cabang             = models.CharField(max_length=250,default=None,blank=True,null=True)
    nama_cabang             = models.CharField(max_length=250,default=None,blank=True,null=True)
    kode_unit               = models.CharField(max_length=50,default=None,blank=True,null=True)
    nama_unit               = models.CharField(max_length=250,default=None,blank=True,null=True)
    tipe_led                = models.TextField(blank=True,null=True)
    kode_produk             = models.CharField(max_length=50,default=None,blank=True,null=True)
    nama_produk             = models.CharField(max_length=250,default=None,blank=True,null=True)
    nama_produk2            = models.CharField(max_length=250,default=None,blank=True,null=True)
    nama_penemu             = models.CharField(max_length=250,default=None,blank=True,null=True)
    kode_ktg_kejadian1      = models.CharField(max_length=250,default=None,blank=True,null=True)
    nama_ktg_kejadian1      = models.CharField(max_length=250,default=None,blank=True,null=True)
    kode_ktg_kejadian2      = models.CharField(max_length=250,default=None,blank=True,null=True)
    nama_ktg_kejadian2      = models.CharField(max_length=250,default=None,blank=True,null=True)
    kode_ktg_kejadian3      = models.CharField(max_length=250,default=None,blank=True,null=True)
    nama_ktg_kejadian3      = models.CharField(max_length=250,default=None,blank=True,null=True)
    kode_penyebab1          = models.CharField(max_length=250,default=None,blank=True,null=True)
    nama_penyebab1          = models.CharField(max_length=250,default=None,blank=True,null=True)
    kode_penyebab2          = models.CharField(max_length=250,default=None,blank=True,null=True)
    nama_penyebab2          = models.CharField(max_length=250,default=None,blank=True,null=True)
    kode_penyebab3          = models.CharField(max_length=250,default=None,blank=True,null=True)
    nama_penyebab3          = models.CharField(max_length=250,default=None,blank=True,null=True)
    bussines_line           = models.CharField(max_length=250,default=None,blank=True,null=True)
    coa_biaya               = models.CharField(max_length=250,default=None,blank=True,null=True)
    mata_uang               = models.CharField(max_length=100,default=None,blank=True,null=True)
    nilai_tukar             = models.CharField(max_length=20,default=None,blank=True,null=True)
    kerugian_potensial      = models.FloatField(default=None,blank=True,null=True)
    rra                     = models.FloatField(default=None,blank=True,null=True)
    recovery                = models.FloatField(default=None,blank=True,null=True)
    kerugian_aktual         = models.FloatField(default=None,blank=True,null=True)
    tanggal_review          = models.DateField(default=None,blank=True,null=True)
    reviewer                = models.CharField(default=None,blank=True,null=True,max_length=20)   
    hasil_review            = models.TextField(default=None,blank=True,null=True)
    keterangan_review       = models.TextField(default=None,blank=True,null=True)
    summary_kejadian        = models.TextField(default=None,blank=True,null=True)
    kronologi_kejadian      = models.TextField(default=None,blank=True,null=True)
    tindakan_unit_kerja     = models.TextField(default=None,blank=True,null=True)
    tindakan_perbaikan      = models.TextField(default=None,blank=True,null=True)
    dibuat_oleh             = models.CharField(max_length=100,default=None,blank=True,null=True)
    ditemukan_oleh          = models.CharField(max_length=100,blank=True,null=True)
    disetujui_oleh          = models.CharField(max_length=100,default=None,blank=True,null=True)
    dihapus                 =models.BooleanField(default=False,blank=True,null=True)
    risiko_kredit           = models.CharField(max_length=20,default=None,blank=True,null=True)
    historis_date           =models.DateTimeField(blank=True,null=True)
    created_at              = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated_at              = models.DateTimeField(auto_now = True,blank=True,null=True)
    def __str__(self):
        return "{}".format(self.nomor_kasus)
    
    
    
    
    


# Create your models here.
