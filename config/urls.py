from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('api/students/', include('students.urls')),
    path('api/sponsors/', include('sponsors.urls')),
    path('api/token/', include('users.urls')),
    path('api/', include('base.urls')),
    path('admin/', admin.site.urls),
]
