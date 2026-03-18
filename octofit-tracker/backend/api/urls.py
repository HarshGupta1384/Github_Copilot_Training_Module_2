from django.urls import path

from . import views

urlpatterns = [
    path('<str:key>/', views.list_items, name='api-list'),
]
