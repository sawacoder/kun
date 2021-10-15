from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
# Create your views here.
from .models import Modelmodel


class HomePageView(TemplateView):
    template_name = 'layout.html'


class NewsView(ListView):
    template_name = 'news.html'
    model = Modelmodel

