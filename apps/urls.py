from django.urls import path
from .views import home, team_member, about_us

urlpatterns = [
    path("", home, name="home"),
    path("teams", team_member, name="team_member"),
    path("about_us", about_us, name="about_us")

]