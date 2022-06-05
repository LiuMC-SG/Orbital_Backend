from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update_db', views.index, name='update_db'),
    path('condensed_info', views.condensed_info, name='condensed_info'),
    path('full_info', views.full_info, name='full_info'),
]
