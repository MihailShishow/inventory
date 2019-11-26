from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class MainTemplateView(TemplateView):
    template_name = 'index.html'


class AboutTemplateView(TemplateView):
    template_name = 'about.html'
