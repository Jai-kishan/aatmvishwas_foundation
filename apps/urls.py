from django.urls import path
from .views import home, team_member

urlpatterns = [
    path("", home, name="home"),
    path("teams", team_member, name="team_member")
]