from django.urls import path

from app_aps.views import contato, home, sobre

urlpatterns = [
    path('', home),
    path('contato/', contato),
    path('sobre/', sobre),
]
