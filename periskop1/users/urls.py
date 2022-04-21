from django.conf.urls import url
from django.urls import path,include
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [

    path('login/',views.loginUser,name= 'loginUser'),
    path('logout/',views.logoutUser,name= 'logout'),
    path('register/',views.registerUser,name= 'register'),
    
]
    