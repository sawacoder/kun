from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import DetailView

#
# # Create your views here.
# class SignUpView(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'registration/signup.html'


class HomeDetailView(DetailView):
    model = Modelmodel
    template_name = 'detail.html'
