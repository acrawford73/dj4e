from django.urls import path
from . import views

app_name = 'autos'
urlpatterns = [

    path("", views.MainView.as_view(), name="all"),

    #path('main/', views.AutosListView.as_view(), name='autos-list'),
    path('main/create/', views.AutosCreateView.as_view(), name='autos-create'),
    path('main/<int:pk>/update/', views.AutosUpdateView.as_view(), name='autos-update'),
    path('main/<int:pk>/delete/', views.AutosDeleteView.as_view(), name='autos-delete'),

    path('lookup/', views.MakeListView.as_view(), name='make-list'),
    path('lookup/create/', views.MakeCreateView.as_view(), name='make-create'),
    path('lookup/<int:pk>/update/', views.MakeUpdateView.as_view(), name='make-update'),
    path('lookup/<int:pk>/delete/', views.MakeDeleteView.as_view(), name='make-delete'),

]