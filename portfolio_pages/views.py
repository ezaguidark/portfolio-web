from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.views.generic import TemplateView, DetailView, ListView, FormView
from. models import Project, Blog
from django.urls import reverse_lazy
from .forms import ContactForm
from django.conf import settings

# Create your views here.

class HomePageView(TemplateView):
    template_name = "home.html"

class AllProjetsView(ListView):
    model = Project
    template_name = "all-projects.html"
    context_object_name = 'projects'

class ProjectDetailView(DetailView):
    model = Project
    template_name = "project.html"
    slug_field = 'urlname'
    slug_url_kwarg = 'urlname'

class BlogPostView(DetailView):
    model = Blog
    template_name = "blog-post.html"
    slug_field = 'urlname'
    slug_url_kwarg = 'urlname'

class SuccessView(TemplateView):
    template_name = "success.html"

# View para poder gestionar un form de contacto
# Necesita utilizar un servidor de correo. ver el archivo settings.py para mas detalles.

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('success')

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        send_mail(
            'Portfolio Page Contact', 
             f'Nombre: {name}\nCorreo electrónico: {email}\nMensaje: {message}',
             email,
             [settings.RECIPIENT_ADDRESS],
             fail_silently=False,
        )
        return super().form_valid(form)