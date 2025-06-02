from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # صفحه اصلی
    path('students/', views.student_list, name='student_list'),  # صفحه لیست دانشجویان
    path('login/', views.student_login, name='login'),  # صفحه لیست دانشجویان
    path('edit/<int:pk>/', views.edit_student, name='edit_student'),
]


