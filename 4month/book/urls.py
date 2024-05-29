from django.urls import path
from . import views
from .views import about_views, hobbies_views, current_time_views, book_view, book_detail_view


urlpatterns = [
    path('hello/', about_views, name='about'),
    path('hobbies/', hobbies_views, name='hobbies'),
    path('current_time/', current_time_views, name='time'),
    path('book/', book_view, name='book'),
    path('book/<int:id>/', book_detail_view, name='book_detail'),
    path('book_list', views.book_list, name='book_list'),
    path('book_list/<int:id>/', views.book_detail, name='book_detail'),
]
