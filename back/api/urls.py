
from django.urls import path, re_path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('/login/', TokenObtainPairView.as_view()),
    path('/refresh/', TokenRefreshView.as_view()),
]