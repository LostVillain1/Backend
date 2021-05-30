from django.urls import path, include
from . import views


urlpatterns = [
    path('person/', views.get_all_persons)
]