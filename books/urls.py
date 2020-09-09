from django.conf.urls import url
from books import views
from django.urls import path, include
#from . import views

urlpatterns = [
    path('books/<endpoint>', views.book_list),
    path('books/', views.book_list),
    path('', views.startpage, name='Start Page'),
]
