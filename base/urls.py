from rest_framework import routers

from base import views

router = routers.DefaultRouter()
router.register(r'credits', views.CreditViewSet, basename='credits')

urlpatterns = router.urls
