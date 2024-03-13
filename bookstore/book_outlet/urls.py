from django.urls import path

from . import views

urlpatterns =[
    path('',views.index,),
    path('<slug:slug>',views.detail_page,name='detail_page')
]