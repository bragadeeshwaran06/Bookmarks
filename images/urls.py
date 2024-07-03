from django.urls import path
from . import views
app_name = 'images'
urlpatterns = [
    path('create/', views.image_create, name='create'),
    path('like/', views.image_like, name='like'),
    path('detail/<int:id>/<slug:slug>/',views.image_detail, name='detail'),
    path('', views.image_list, name='list'),
    path('ranking/', views.image_ranking, name='ranking'),
]

#https://127.0.0.1:8000/images/create/?title=%20Django%20and%20Duke&url=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2F8%2F85%2FDjango_Reinhardt_and_Duke_Ellington_%28Gottlieb%29.jpg
