from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView, DetailView

from .models import Modelmodel, Rightmodel


# class NewsView(ListView):
#     template_name = 'news.html'
#     model = Modelmodel


def right(request):
    right = Rightmodel.objects.all()
    content = Modelmodel.objects.all()
    obj = Modelmodel.objects.latest('id')
    return render(request, 'news.html', {'content': content, 'right': right, 'obj': obj})


def detail(request, pk):
    content = Modelmodel.objects.get(pk=pk)
    left = Modelmodel.objects.all()
    right = Rightmodel.objects.all()
    return render(request, 'detail.html', {'left': left, 'right': right, 'content': content})


# class detail(DetailView):
#     model = Modelmodel
#     template_name = 'detail.html'


def right_detail(request, pk):
    right = Rightmodel.objects.get(pk=pk)
    left = Modelmodel.objects.all()
    right_model = Rightmodel.objects.all()
    return render(request, 'right_detail.html', {'left': left, 'right_model': right_model, 'right': right})

# class right_detail(DetailView):
#     model = Rightmodel
#     template_name = 'right_detail.html'
