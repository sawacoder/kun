from django.urls import path
from .views import detail, right, right_detail





urlpatterns = [
    # path('', NewsView.as_view(), name='home'),
    path('', right, name='right'),
    path('detail/<int:pk>/', detail, name='detail'),
    path('right/<int:pk>/', right_detail, name='right_detail')
]
