from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<slug:slug>/', views.article),
    path('<slug:slug>/content', views.article_only_content),

]