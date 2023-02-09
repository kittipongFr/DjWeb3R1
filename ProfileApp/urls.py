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
path('inputProduct/', views.inputProduct, name='inputProduct'),
path('listProduct/', views.listProduct, name='listProduct'),
path('pro_retriveAll/', views.product_retriveAll, name='pro_retriveAll'),
path('pro_retriveOne/<pid>', views.product_retriveOne, name='pro_retriveOne'),
path('createProduct/', views.createProduct, name='createProduct'),
path('updateProduct/<pid>', views.updateProduct, name='updateProduct'),
path('deleteProduct/<pid>', views.deleteProduct, name='deleteProduct'),
path('showGoodsAll/', views.showGoodsAll, name='showGoodsAll'),
path('showGoodsOne/<gid>', views.showGoodsOne, name='showGoodsOne'),
path('showCusAll/', views.showCusAll, name='showCusAll'),
path('showCusOne/<cid>', views.showCusOne, name='showCusOne'),
path('newGoods/', views.newGoods, name='newGoods'),
path('updateGoods/<gid>', views.updateGoods, name='updateGoods'),
path('deleteGoods/<gid>', views.deleteGoods, name='deleteGoods'),
path('newCus/', views.newCus, name='newCus'),
path('updateCus/<cid>', views.updateCus, name='updateCus'),
path('deleteCus/<cid>', views.deleteCus, name='deleteCus'),
    ]