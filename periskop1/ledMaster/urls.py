from django.conf.urls import url
from django.urls import path,include
from . import views
import debug_toolbar
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [

    path('listHistori/',views.listHistori,name= 'listHistori'),
    path('showHistori/<int:lapId>/',views.showHistori,name='showHistori'),
    path('exportHistori/<int:lapId>/<int:hsId>/',views.exportHistori,name='exportHistori'),
    path('__debug__/',include(debug_toolbar.urls)),
]
