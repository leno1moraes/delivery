from django.urls import path

from .views import index, contato
urlpatterns = [
    path('', index),
    path('index', index),
    path('contact', contato),
]