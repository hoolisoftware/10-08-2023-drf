from django.urls import path

from . import views


urlpatterns = [
    path('request_parsing/', views.request_parsing),
    path('content_negotiation/', views.content_negotiation),
]
