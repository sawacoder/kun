from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include


def home(request):
    return redirect(to="yangiliklar:news")


urlpatterns = [
    path('', home, name='home'),
    path('news/', include('yangiliklar.urls')),
    path('admin/', admin.site.urls),
]
