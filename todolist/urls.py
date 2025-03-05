from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.views.auth import RegisterView

urlpatterns = [
    # Checklist Endpoints
    path("", include("api.urls")),
    # Authentication Endpoints
    path("login", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("register", RegisterView.as_view(), name="register"),
]
