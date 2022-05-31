from django.urls import path
from .views import *

urlpatterns = [
    path('', ParametersCreateView.as_view(), name='home'),
    path('history/', HistoryView.as_view(), name='history'),
    path('<int:pk>/edit', ParametersUpdateView.as_view(), name='update'),
    path('<int:pk>/remove', ParametersDeleteView.as_view(), name='delete'),
    path('<int:pk>/send', ParametersSendView.as_view(), name='send'),

]
