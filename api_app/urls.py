from django.urls import path, include


app_name = "api_app"

urlpatterns = [
    path("user/", include("auth_app.urls", namespace="auth_app")),
    path("catalog/", include("catalog_app.urls", namespace="catalog_app")),
    path("cart/", include("cart_app.urls", namespace="cart_app")),
]
