"""Defines url patterns for learning_logs."""

from django.urls import path

from . import views

app_name = 'app_test'
urlpatterns = [
    # Home page.
    path('', views.index, name='index'),
]