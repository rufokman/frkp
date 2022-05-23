from django.urls import path
from . import views
urlpatterns = [
    path('', views.parameters_view, name='home')
]
