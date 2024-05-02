from django.views.generic import TemplateView

class Home(TemplateView):
    template_name = "pages/home.html"

class About(TemplateView):
    template_name = "pages/about.html"

class Projects(TemplateView):
    template_name = "pages/projects.html"

class Contact(TemplateView):
    template_name = "pages/contact.html"