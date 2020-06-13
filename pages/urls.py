# pages/urls.py
from django.urls import path
from . import views
app_name = "pages"

urlpatterns = [
    path('index/', views.index, name="index"),
    path('hello/', views.hello, name="hello"),
    path('name/', views.name, name="name"),
    path('introduce/', views.introduce, name="introduce"),
    path('classRandomChoice/', views.classRandomChoice, name="classRandomChoice"),
    path('yourname/<str:name>/', views.yourname, name="yourname"),
    path('urlcopy/<str:name>/<int:age>', views.urlcopy, name="urlcopy"),
    path('multiply/<int:num1>/<int:num2>', views.multiply, name="multiply"),
    path('multipletable/<int:big>/<int:small>', views.multipletable, name="multipletable"),
    path('dtl/', views.dtl, name="dtl"),
    path('forif/', views.forif, name="forif"),
    path('loop/', views.loop, name="loop"),
    path('throw/', views.throw, name="throw"),
    path('catch/', views.catch, name="catch"),
    path('lottoT/', views.lottoT, name="lottoT"),
    path('lottoC/', views.lottoC, name="lottoC"),
    path('artii/', views.artii, name="artii"),
    path('result/', views.result, name="result"),
]
