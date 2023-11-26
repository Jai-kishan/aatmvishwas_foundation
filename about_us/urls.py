from django.urls import path
from about_us import views

urlpatterns = [
    path('about_us/', views.about_us_list),
    path('about_us/<int:pk>/', views.about_us_detail),
]