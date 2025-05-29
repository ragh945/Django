from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # default to current month/year
    path('<int:year>/<int:month>/', views.index, name='calendar_month'),  # dynamic month/year view
]
