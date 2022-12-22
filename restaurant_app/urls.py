from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('table/', views.table, name='table'),
    path('feedback/', views.feedback, name='feedback'),
    path('about_us/', views.about_us, name='about_us'),
    path('create_feedback/', views.create_feedback, name='create_feedback'),
    # path('ссылка на страницу', views.asd что-то из views.py (asd) , name = '' подключение ссылки на странице,
]
