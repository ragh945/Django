from django.urls import path
from . import views  # This is correct here

urlpatterns = [
    path('index/', views.index, name='index'),
]
