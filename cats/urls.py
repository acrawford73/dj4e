from django.urls import path
from . import views

app_name = 'cats'

urlpatterns = [

    path('', views.CatList.as_view(), name='cat-all'),
    path('main/create/', views.CatCreate.as_view(), name='cat-create'),
    path('main/<int:pk>/update/', views.CatUpdate.as_view(), name='cat-update'),
    path('main/<int:pk>/delete/', views.CatDelete.as_view(), name='cat-delete'),

    path('lookup/', views.BreedList.as_view(), name='breed-list'),
    path('lookup/create/', views.BreedCreate.as_view(), name='breed-create'),
    path('lookup/<int:pk>/update/', views.BreedUpdate.as_view(), name='breed-update'),
    path('lookup/<int:pk>/delete/', views.BreedDelete.as_view(), name='breed-delete'),

]