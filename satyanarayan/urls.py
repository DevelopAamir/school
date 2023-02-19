from django.urls import path, include
from satyanarayan import views

urlpatterns = [
    path('', views.index, name='home'),
    path('posts', views.posts, name='posts'),
    path('post/<str:id>/', views.viewposts, name='viewposts'),
    path('contacts', views.contacts, name='contacts'),

]