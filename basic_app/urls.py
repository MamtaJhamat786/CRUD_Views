from django.urls import path
from . import views

# TEMPLATE URLS

app_name= 'basic_app'

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('home/',views.IndexView.as_view(), name='index'),
    path('school/',views.SchoolListView.as_view(), name='list'),
    path('school/<pk>/',views.SchoolDetailView.as_view(), name="detail"),
    path("create/", views.SchoolCreateView.as_view(), name="create"),
    path('update/<pk>/',views.SchoolUpdateView.as_view(), name="update"),
    path('delete/<pk>/',views.SchoolDeleteView.as_view(), name="delete"),
   
]
