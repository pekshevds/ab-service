from django.http import HttpRequest
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from cart_app.services import (
    get_cart,
    add_to_cart,
    delete_from_cart,
    clear_cart,
    set_to_cart,
    send_cart,
)


class CartView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request: HttpRequest):
        response = get_cart(request)
        return Response(response)


class CartAddView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request: HttpRequest):
        add_to_cart(request)
        response = get_cart(request)
        return Response(response)


class CartSetView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request: HttpRequest):
        set_to_cart(request)
        response = get_cart(request)
        return Response(response)


class CartDeleteView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request: HttpRequest):
        delete_from_cart(request)
        response = get_cart(request)
        return Response(response)


class CartClearView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request: HttpRequest):
        clear_cart(request)
        response = get_cart(request)
        return Response(response)


class CartSendView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request: HttpRequest):
        if send_cart(get_cart(request)):
            clear_cart(request)
        response = get_cart(request)
        return Response(response)
