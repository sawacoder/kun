from django.urls import path
from .views import (contact_list_page,
                    details,
                    create_page,
                    create,
                    delete,
                    delete_page,
                    add_page,
                    add)
app_name = 'contact'
urlpatterns = [
    path('list/', contact_list_page, name='contact'),
    path('add_page/<int:pk>/', add_page, name='add_page'),
    path('add/<int:pk>/', add, name='add'),
    path('details/<int:pk>/', details, name='detail'),
    path('create_page/', create_page, name='create_page'),
    path('create/', create, name='create'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('delete_page/<int:pk>/', delete_page, name='delete_page'),

]
