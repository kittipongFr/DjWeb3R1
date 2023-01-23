from django.urls import path
from ProfileApp import views


urlpatterns = [

path('firstweb/', views.firstweb, name='firstweb'),
path('secondpage/', views.secondpage, name='secondpage'),
path('thirdpage/', views.thirdpage, name='thirdpage'),
path('product/', views.product, name='product'),
path('idol/', views.idol, name='idol'),
path('showmydata/', views.showmydata, name='showmydata'),
path('showOurproduct/', views.showProduct, name='showOurproduct'),
path('newProduct/', views.newProduct, name='newProduct'),
path('frmProduct/', views.frmproduct, name='frmProduct'),
    ]