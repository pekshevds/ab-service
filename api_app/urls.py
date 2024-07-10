from django.urls import path, include
from rest_framework.authtoken import views


app_name = "api_app"

urlpatterns = [
    path("catalog/", include("catalog_app.urls", namespace="catalog_app")),
    path("cart/", include("cart_app.urls", namespace="cart_app")),
    path("api-token-auth/", views.obtain_auth_token),
]
