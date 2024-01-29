from django.urls import path

from rest_framework import routers

from base.views import CreditViewSet, DashboardView

router = routers.DefaultRouter()
router.register(r'credits', CreditViewSet, basename='credits')


urlpatterns = [
    path('dashboard/', DashboardView.as_view())
]


urlpatterns += router.urls
