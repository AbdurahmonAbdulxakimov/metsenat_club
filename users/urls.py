from django.urls import path
from .views import TokenObtainPairView, TokenRefreshView


app_name = 'user'

urlpatterns = [
    path('', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
