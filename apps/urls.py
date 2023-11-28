from django.urls import path
from .views import home, team_member, about_us, contact_us, blogs, donate_us

urlpatterns = [
    path("", home, name="home"),
    path("teams", team_member, name="team_member"),
    path("about_us", about_us, name="about_us"),
    path("contact_us", contact_us, name="contact_us"),
    path("blog", blogs, name="blogs"),
    path("donate_us", donate_us, name="donate_us"),

]