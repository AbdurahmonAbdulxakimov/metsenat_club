from rest_framework import routers

from students import views


router = routers.DefaultRouter()
router.register(r'', views.StudentViewSet, basename='student')

urlpatterns = router.urls
