from django.urls import path
from .views import home

app_name = 'papers'

urlpatterns = [
    path('', home, name='home'),
]
