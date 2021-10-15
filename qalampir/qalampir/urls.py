from django.urls import path
from .views import HomePageView,NewsView
# def get_filename(filename):
#     return filename.upper()

urlpatterns = [
    path('', NewsView.as_view(), name='home')
]
