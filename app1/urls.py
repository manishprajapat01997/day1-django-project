from django.urls import path
from .views import *

urlpatterns = [

    path('add/', add_employee, name='add_url'),
    path('show/', show_employee, name='show_url'),
    path('update/<int:pk>/', update_employee, name='update_url'),
    path('delete/<int:pk>/', delete_employee, name='delete_url'),
]