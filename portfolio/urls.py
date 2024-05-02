from django.urls import path
from .views import Home, About, Projects, Contact

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("about", About.as_view(), name="about"),
    path("projects", Projects.as_view(), name="projects"),
    path("contact", Contact.as_view(), name="contact"),
]
