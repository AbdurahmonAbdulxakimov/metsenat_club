from rest_framework import routers

from sponsors import views 


router = routers.DefaultRouter()
router.register(r'', views.SponsorViewSet, basename='sponsors')

urlpatterns = router.urls