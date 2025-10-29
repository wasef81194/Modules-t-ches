from django.urls import path
from .views import home,new

urlpatterns = [
    path('', home, name='home'),
    path('taches/new', new, name='new'),
]