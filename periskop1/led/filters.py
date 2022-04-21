from webbrowser import get
from django.contrib.auth.models import User

from .models import Cabang, Coa, Led,Laporan,LedLaporan,KategoriKejadian,Penyebab, StateChange, SummaryKejadian, Unit,BusinessLine,Produk,KategoriLaporan,Perubahan,Journal
import django_filters

class SearchFilter(django_filters.FilterSet):
    
    # kerugian_potensial__gt= django_filters.NumberFilter(name='kerugian_potensial', lookup_expr='kerugian')
    class Meta:
        
        model = Led
        fields = ['nomor_kasus','tanggal_kejadian']
    
    @property
    def qs(self):
        parent= super().qs
        tipe= getattr(self.request,'tipe_led',"fl")
        kerugianlt = getattr(self.request,'kerugian_potensial',300000000)
        kerugiangt = getattr(self.request,'kerugian_potensial',5000000)
        print(tipe)
        
        return parent.filter(tipe_led__iexact= tipe, kerugian_potensial__lt= kerugianlt,kerugian_potensial__gte=kerugiangt)
        
        