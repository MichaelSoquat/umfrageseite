from django.urls import URLPattern, path
from .views import index, umfrage_detail

urlpatterns = [
    path('', index),
    path('abstimmung/<str:slug>', umfrage_detail)
]