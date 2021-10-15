from django.urls import path
from yangiliklar.views import (
    post_list_page,
    post_create,
    post_create_page,
    post_detail_page)

app_name = 'yangiliklar'

urlpatterns = [
    path('', post_list_page, name='news'),
    path('post_create/', post_create, name='post_create'),
    path('post_create_page/', post_create_page, name='post_create_page'),
    path('post_detail_page/<int:post_id>', post_detail_page, name='post_detail_page'),
]
