from django.urls import path
from choujiang import views

urlpatterns = [
    path('index/choujiang/1/', views.choujiang_1, name='choujiang1'),
    path('index/choujiang/2/', views.choujiang_2, name='choujiang2'),
    path('index/choujiang/3/', views.choujiang_3, name='choujiang3'),
    path('index/choujiang/result/', views.result_all, name='result_all'),
    path('index/choujiang/1/result/', views.result_1, name='result_1'),
    path('index/choujiang/2/result/', views.result_2, name='result_2'),
    path('index/choujiang/3/result/', views.result_3, name='result_3'),
]