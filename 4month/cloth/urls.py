from django.urls import path
from . import views

urlpatterns = [
    path('all_cloth/', views.AllClothView.as_view(), name='all_cloth'),
    path('male/', views.MenClothView.as_view(), name='Men'),
    path('female/', views.WomenClothView.as_view, name='Women'),
    path('kids/', views.KidsClothView.as_view(), name='Kids'),
]

