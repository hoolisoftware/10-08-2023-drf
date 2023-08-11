from django.urls import path

from . import views


urlpatterns = [
    path('creating_responses/', views.creating_responses),
    path('attributes/', views.attributes),
]