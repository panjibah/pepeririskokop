from turtle import mode
from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.db.models.deletion import CASCADE
from django.db.models.fields import BooleanField, DateField, IntegerField
from django.db.models.fields import related
from django.db.models.fields.related import ForeignKey
from softdelete.models import SoftDeleteObject
#belum dilakukan
#indexing nomor kasus dan semua kode
#nggak usah pake foreign key
#BUAT TABLE BARU UNTUK SIMPAN PRODUK LEVEL 2 DAN SETERUSNYA? YANG REFENECRE TABLE IUTAMA

class KategoriKejadian(models.Model):
    kode_kategori1 = models.CharField(max_length=255,blank=True,null=True)
    nama_kategori1 = models.CharField(max_length = 255,blank=True,null=True)
    kode_kategori2 = models.CharField(max_length=255,blank=True,null=True)
    nama_kategori2 = models.CharField(max_length = 255,blank=True,null=True)
    kode_kategori3 = models.CharField(max_length=255,blank=True,null=True)
    nama_kategori3 = models.CharField(max_length = 255,blank=True,null=True)
    status = models.BooleanField(default=1,blank=True,null=True)
    update_date = models.DateField(blank=True,null=True) 
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now = True)
    def __str__(self):
        return "{}".format(self.kode_kategori1)

class Penyebab(models.Model):
    kode_penyebab1 = models.CharField(max_length=20,blank=True,null=True)
    nama_penyebab1 = models.CharField(max_length = 255,blank=True,null=True)
    kode_penyebab2 = models.CharField(max_length=20,blank=True,null=True)
    nama_penyebab2 = models.CharField(max_length = 255,blank=True,null=True)
    kode_penyebab3 = models.CharField(max_length=20,blank=True,null=True)
    nama_penyebab3 = models.CharField(max_length = 255,blank=True,null=True)
    status = models.BooleanField(default=1,blank=True,null=True)
    update_date = models.DateField(blank=True,null=True)    
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now = True)
    def __str__(self):
        return "{}".format(self.kode_penyebab3)

class Unit(models.Model):
    kode_unit = models.CharField(max_length=255)
    nama_unit = models.CharField(max_length = 250)
    update_date = models.DateField(blank=True,null=True) 
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now = True)
    def __str__(self):
        return "{}".format(self.kode_unit)

class Cabang(models.Model):
    kode_cabang = models.CharField(max_length=255)
    tipe_cabang = models.CharField(max_length = 255)
    nama_cabang = models.CharField(max_length=250)
    segmentasi  = models.CharField(max_length=255)
    status      = models.CharField(max_length=255)
    update_date = models.DateField(blank=True,null=True) 
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return "{}".format(self.kode_cabang)
    
    
class BusinessLine(models.Model):
    kode_bisnis = models.CharField(max_length = 255)
    nama = models.CharField(max_length= 250)
    status = models.CharField(max_length = 250)
    update_date = models.DateField(blank=True,null=True) 
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now = True)
    def __str__(self):
        return "{}".format(self.kode_bisnis)

class Produk (models.Model):
    kode_produk = models.CharField(max_length =255)
    tipe_produk = models.CharField(max_length=50)
    nama_produk = models.CharField(max_length=250)
    status = models.CharField(max_length=250)
    update_date = models.DateField(blank=True,null=True) 
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now = True)
    def __str__(self):
        return "{}".format(self.kode_produk)
    
class Coa(models.Model):
    kode_coa = models.CharField(max_length=255)
    nama = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    update_date = models.DateField(blank=True,null=True) 
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now = True)
    def __str__(self):
        return "{}".format(self.nama)
#rra reference
#perlu email -> 0 = tidak perlu 1= perlu 


class Led(models.Model):
    nomor_kasus             =  models.CharField(max_length =255)
    tanggal_kejadian        = models.DateField(default=None,blank=True,null=True)
    tanggal_teridentifikasi = models.DateField(default=None,blank=True,null=True)
    tanggal_input           = models.DateField(default=None,blank=True,null=True)
    tanggal_selesai         = models.DateField(default=None,blank=True,null=True)
    tanggal_update          = models.DateTimeField(default=None,blank=True,null=True)
    jumlah_kasus            = models.IntegerField(default=None,blank=True,null=True)
    nama_pembuat            = models.CharField(max_length=255,default=None,blank=True,null=True)
    status                  = models.CharField(max_length=50,default=None,blank=True,null=True)
    kode_cabang             = models.ForeignKey(Cabang,on_delete=models.CASCADE,default=None,blank=True,null=True)
    kode_unit               = models.CharField(max_length=255,default=None,blank=True,null=True)
    tipe_led                = models.TextField(blank=True,null=True)
    kode_produk             = models.ForeignKey(Produk,on_delete=models.CASCADE,default=None,blank=True,null=True)
    nama_penemu             = models.CharField(max_length=255,default=None,blank=True,null=True)
    kode_ktg_kejadian       = ForeignKey(KategoriKejadian,on_delete=models.CASCADE,default=None,blank=True,null=True)
    kode_penyebab           = models.ForeignKey(Penyebab,on_delete=models.CASCADE,default=None,blank=True,null=True)
    business_line           = models.ForeignKey(BusinessLine,on_delete=models.CASCADE,default=None,blank=True,null=True)
    coa_biaya               = models.ForeignKey(Coa,on_delete=models.CASCADE,default=None,blank=True,null=True)
    mata_uang               = models.CharField(max_length=255,default=None,blank=True,null=True)
    nilai_tukar             = models.FloatField(default=None,blank=True,null=True)
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
    dibuat_oleh             = models.CharField(max_length=255,default=None,blank=True,null=True)
    ditemukan_oleh          = models.CharField(max_length=255,blank=True,null=True)
    disetujui_oleh          = models.CharField(max_length=255,default=None,blank=True,null=True)
    dihapus                 =models.BooleanField(default=False,blank=True,null=True)
    chk_kknled              =models.BooleanField(default=False,blank=True,null=True)
    chk_summ                =models.BooleanField(default=False,blank=True,null=True)
    risiko_kredit           = models.CharField(max_length=255,default=None,blank=True,null=True)
    review_user             = models.CharField(max_length=100,default='Belum Review',blank=True,null=True)
    perlu_email             = models.IntegerField(default=0,blank=True,null=True)
    created_at              = models.DateTimeField(auto_now_add=True)
    updated_at              = models.DateTimeField(auto_now = True)
    def __str__(self):
        return "{}".format(self.nomor_kasus)

class Kasus(models.Model):
    nomor_kasus             =  models.CharField(max_length =255)
    tanggal_kejadian        = models.DateField(default=None,blank=True,null=True)
    tanggal_teridentifikasi = models.DateField(default=None,blank=True,null=True)
    tanggal_input           = models.DateField(default=None,blank=True,null=True)
    tanggal_selesai         = models.DateField(default=None,blank=True,null=True)
    tanggal_update          = models.DateTimeField(default=None,blank=True,null=True)
    jumlah_kasus            = models.IntegerField(default=None,blank=True,null=True)
    nama_pembuat            = models.CharField(max_length=255,default=None,blank=True,null=True)
    status                  = models.CharField(max_length=50,default=None,blank=True,null=True)
    kode_cabang             = models.CharField(max_length=255,default=None,blank=True,null=True)
    nama_cabang             = models.TextField(default=None,blank=True,null=True)
    kode_unit               = models.CharField(max_length=255,default=None,blank=True,null=True)
    nama_unit               = models.TextField(default=None,blank=True,null=True)
    tipe_led                = models.TextField(blank=True,null=True)
    nama_produk             = models.CharField(max_length=255,default=None,blank=True,null=True)
    nama_penemu             = models.CharField(max_length=255,default=None,blank=True,null=True)
    kode_ktg_kejadian       = models.CharField(max_length=255,default=None,blank=True,null=True)
    kode_penyebab           = models.CharField(max_length=255,default=None,blank=True,null=True)
    business_line           = models.CharField(max_length=255,default=None,blank=True,null=True)
    coa_biaya               = models.CharField(max_length=255,default=None,blank=True,null=True)
    mata_uang               = models.CharField(max_length=255,default=None,blank=True,null=True)
    nilai_tukar             = models.FloatField(default=None,blank=True,null=True)
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
    dibuat_oleh             = models.CharField(max_length=255,default=None,blank=True,null=True)
    ditemukan_oleh          = models.CharField(max_length=255,blank=True,null=True)
    disetujui_oleh          = models.CharField(max_length=255,default=None,blank=True,null=True)
    dihapus                 =models.BooleanField(default=False,blank=True,null=True)
    chk_kknled              =models.BooleanField(default=False,blank=True,null=True)
    chk_summ                =models.BooleanField(default=False,blank=True,null=True)
    risiko_kredit           = models.CharField(max_length=255,default=None,blank=True,null=True)
    review_user             = models.CharField(max_length=100,default='Belum Review',blank=True,null=True)
    perlu_email             = models.IntegerField(default=0,blank=True,null=True)
    created_at              = models.DateTimeField(auto_now_add=True)
    updated_at              = models.DateTimeField(auto_now = True)
    def __str__(self):
        return "{}".format(self.nomor_kasus)
       
    
class SummaryKejadian(models.Model):
    kategori = models.TextField()
    nama_lv1        = models.DateTimeField(auto_now_add=True)
    summ_ormis         = models.TextField(default=None,blank=True,null=True)
    summ_ormc           =models.TextField(default=None,blank=True,null=True)
    catatan = models.TextField(default=None,blank=True,null=True)
    created_at              = models.DateTimeField(auto_now_add=True)
    updated_at              = models.DateTimeField(auto_now = True)
    def __str__(self):
        return "{}".format(self.nama)


class KategoriLaporan(models.Model):
    nama = models.TextField()
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now = True)
    def __str__(self):
        return "{}".format(self.nama)

#tanggal jurnal
class Journal(models.Model):
    nomor_kasus= models.TextField()
    tanggal_jurnal          = models.DateTimeField(blank=True,null=True)
    debet_kredit         =  models.TextField(default=None,blank=True,null=True)
    kode_mata_uang      = models.CharField(max_length=20,default=None,blank=True,null=True)
    jumlah_nominal_asal =   models.FloatField(default=None,blank=True,null=True) 
    jumlah_nominal_idr =   models.FloatField(default=None,blank=True,null=True)
    keterangan         =  models.TextField(default=None,blank=True,null=True)
    kode_coa =   models.TextField(default=None,blank=True,null=True)       
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now = True)
    def __str__(self):
        return "{}".format(self.nomor_kasus)
    
#hapus foreign key
class Laporan(models.Model):
    nama            = models.TextField()
    periode_awal    = models.DateField()
    periode_akhir   = models.DateField()
    kategori        = models.ForeignKey(KategoriLaporan,on_delete=models.CASCADE)
    ks_belumrv        = models.IntegerField(default=0,blank=True,null=True)
    ks_save         = models.IntegerField(default=0,blank=True,null=True)
    ks_submit       = models.IntegerField(default=0,blank=True,null=True)
    creator         = models.TextField(default='')
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now = True)
    def __str__(self):
        return "{}".format(self.nama)
    
class KasusLaporan(models.Model):
    laporan_id             = models.BigIntegerField(default=0,blank=True,null=True)
    kasus_id                = models.BigIntegerField(default=0,blank=True,null=True)
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now = True)
    def __str__(self):
        return "{}".format(self.laporan) 
   
class LedLaporan(models.Model):
    laporan             = models.ForeignKey(Laporan,on_delete=models.CASCADE)
    led_laporan         = models.ForeignKey(Led,on_delete=models.CASCADE)
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now = True)
    def __str__(self):
        return "{}".format(self.laporan) 

class StateChange(models.Model):
    nomor_kasus = models.ForeignKey(Led,on_delete=models.CASCADE,related_name='nomorKasus')
    nomor_kasus2 =models.ForeignKey(Led,on_delete=models.CASCADE,related_name='nomorKasus2')
    nama_kolom = models.CharField(max_length=50)
    value = models.TextField()
    status = models.CharField(max_length=50)
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now = True)
    def __str__(self):
        return "{}".format(self.nomor_kasus)

#belum ditambah user
class Perubahan(models.Model):  
    nomor_kasus = models.ForeignKey(Led,on_delete=models.CASCADE)
    nama_kolom  = models.TextField(blank=True,null=True)
    data_lama   = models.TextField(blank=True,null=True)
    data_baru   = models.TextField(blank=True,null=True)
    status      = models.CharField(max_length=50,blank=True,null=True)
    alasan      = models.TextField(blank=True,null=True)
    reviewer    = models.TextField(blank=True,null=True)
    user        = models.CharField(max_length=255,blank=True,null=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now = True)
    def __str__(self):
        return "{}".format(self.nomor_kasus)

# Create your models here.
