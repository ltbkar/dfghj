from django.urls import path
from . import views
from .views import about_views
from .views import hobbies_views
from .views import current_time_views

urlpatterns = [
    path('hello/', about_views, name='about'),
    path('hobbies/', hobbies_views, name='hobbies'),
    path('current_time/', current_time_views, name='time'),
    path('book_view/', views.BookView.as_view, name='book'),
    path('book_detail/<int:id>/', views.BookDetail.as_view, name='book'),
    path('book_list/', views.BookListView.as_view(), name='book_list'),
    path('book_list/<int:id>/', views.BookDetailView.as_view(), name='book_detail'),
    path('create_book/', views.CreateBookView.as_view, name='create'),
]
