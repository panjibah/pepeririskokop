from django.conf.urls import url
from django.urls import path,include
from . import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('',views.listLed),
    path('listLed/',views.listLed,name= 'listLed'),
    path('createReport/',views.createReport,name='createRpt'),
    path('listReport/',views.listReport,name='listRpt'),
    path('listLedReport/<int:rptId>/',views.listLedReport,name='listLedReport'),
    path('kerugian/<int:rptId>/<int:tipe>/',views.kerugian,name='kerugian'),
    path('testJson/',views.testJson,name='testJson'),
    path('reviewLed/',views.reviewLed,name='reviewLed'),
    path('reviewLedId/<int:ledId>/',views.reviewLedId,name='reviewLedId'),
    path('deepDiff/',views.deepDiff,name = 'deepDiff'),
    path('getChange/',views.getStateChange,name = 'getChange'),
    path('replace/<int:ledId>/<int:ledId2>',views.replace,name = 'replace'),
    path('editLed/<int:ledId>',views.editLed,name="editLed"),
    path('updateLed/<int:ledId>',views.updateLed,name="updateLed"),
    path('cabang/',views.listCabang,name='listCabang'),
    path('produk/',views.listProduk,name='listProduk'),
    path('kejadian/',views.listKejadian,name='listKejadian'),
    path('penyebab/',views.listPenyebab,name='listPenyebab'),
    path('businessLine/',views.listBusinessLine,name='listBusinessLine'),
    path('coa/',views.listCoa,name='listCoa'),
    path('export/<int:ledId>/',views.exportLaporan,name='export'),
    path('compImport/',views.iptKtgKejadian,name='compImport'),
    path('perubahanLaporan/<int:lapId>/',views.showPerubahanLaporan,name='perubahanLaporan'),
    path('deleteStateChange/<int:ledId>/<int:scId>',views.deleteStateChange2,name='delStateChange'),
    path('searchLed/<int:lapId>/',views.searchLed,name ='searchLed'),
    path('searchLedAjx/',views.searchLedAjx,name ='searchLedAjx'),
    path('deleted/',views.deleteLedBySystems,name ='deleted'),
    path('ledHistori/<int:lapId>/',views.createLedHistory,name='ledHistori'),
    path('xlsx',views.xlsToXlsx,name='xlsx'),
    path('importkk/',views.importKtgKejadian,name='importKK'),
    path('import/',views.importJrl,name='importKK'),
    path('importAll/',views.importAll,name='importAll'),
    path('kerugian/',views.getKerugian,name='krg'),
    path('summRpt/<int:rptId>/',views.summaryReport,name='summRpt'),
    path('dummy/',views.dummy,name='dummy'),
    path('filterSearch/',views.filterSearch,name='filterSearch'),
]   
    