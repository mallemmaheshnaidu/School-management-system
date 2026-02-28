from django.urls import path
from . import views

app_name = 'school'

urlpatterns = [
    # new dashboard view at root
    path('', views.dashboard, name='dashboard'),
    path('students/', views.StudentListView.as_view(), name='student_list'),
    path('student/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),

    # informational pages
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('reviews/', views.reviews, name='reviews'),
]
