from django.urls import path
from . import views

app_name = 'employee'
urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.AuthLoginView.as_view(), name='login'),
    path('logout/', views.AuthLogOutView.as_view(), name='logout'),
    path('employee_list/', views.EmployeeListView.as_view(), name='employee_list'),

]
