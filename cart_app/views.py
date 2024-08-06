from decimal import Decimal
from django.http import HttpRequest
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from auth_app.serializers import TokenSerializer
from cart_app.serializers import CartSerializer
from cart_app.services import (
    get_token,
    get_good,
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
        response = {"data": None}
        token = request.GET.get("token")
        serializer = TokenSerializer(data={"token": token})
        if serializer.is_valid(raise_exception=True):
            serializer = CartSerializer(
                get_cart(token=get_token(token=token)), many=True
            )
            response["data"] = serializer.data
        return Response(response)


class CartAddView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request: HttpRequest):
        response = {"data": None}
        token = request.GET.get("token")
        serializer = TokenSerializer(data={"token": token})
        if serializer.is_valid(raise_exception=True):
            token = get_token(token=token)
            add_to_cart(
                token=token,
                good=get_good(good_id=request.GET.get("id")),
                qnt=Decimal(request.GET.get("qnt", "1")),
            )
            serializer = CartSerializer(get_cart(token=token), many=True)
            response["data"] = serializer.data
        return Response(response)


class CartSetView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request: HttpRequest):
        response = {"data": None}
        token = request.GET.get("token")
        serializer = TokenSerializer(data={"token": token})
        if serializer.is_valid(raise_exception=True):
            token = get_token(token=token)
            set_to_cart(
                token=token,
                good=get_good(good_id=request.GET.get("id")),
                qnt=Decimal(request.GET.get("qnt", "1")),
            )
            serializer = CartSerializer(get_cart(token=token), many=True)
            response["data"] = serializer.data
        return Response(response)


class CartDeleteView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request: HttpRequest):
        response = {"data": None}
        token = request.GET.get("token")
        serializer = TokenSerializer(data={"token": token})
        if serializer.is_valid(raise_exception=True):
            token = get_token(token=token)
            delete_from_cart(
                token=token,
                good=get_good(good_id=request.GET.get("id")),
                qnt=Decimal(request.GET.get("qnt", "1")),
            )
            serializer = CartSerializer(get_cart(token=token), many=True)
            response["data"] = serializer.data
        return Response(response)


class CartClearView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request: HttpRequest):
        response = {"data": None}
        token = request.GET.get("token")
        serializer = TokenSerializer(data={"token": token})
        if serializer.is_valid(raise_exception=True):
            token = get_token(token=token)
            clear_cart(token=token)
            serializer = CartSerializer(get_cart(token=token), many=True)
            response["data"] = serializer.data
        return Response(response)


class CartSendView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request: HttpRequest):
        response = {"data": None}
        token = request.GET.get("token")
        serializer = TokenSerializer(data={"token": token})
        if serializer.is_valid(raise_exception=True):
            token = get_token(token=token)
            if send_cart(get_cart(token=token)):
                clear_cart(token=token)
            serializer = CartSerializer(get_cart(token=token), many=True)
            response["data"] = serializer.data
        return Response(response)

    def post(self, request: HttpRequest):
        response = {"data": None}
        return Response(response)
