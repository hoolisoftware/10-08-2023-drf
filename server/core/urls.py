from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ep_requests/', include('apps.ep_requests.urls')),
    path('ep_responses/', include('apps.ep_responses.urls')),
]
