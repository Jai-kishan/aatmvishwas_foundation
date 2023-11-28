from django.urls import path
from .views import about_us

urlpatterns = [
    # path('about_us/', views.about_us_list),
    # path('about_us/<int:pk>/', views.about_us_detail),
    path("about_us", about_us, name="about_us")

]