from rest_framework import permissions, authentication
from rest_framework.views import APIView
from rest_framework.response import Response
from auth_app.models import User, Token
from auth_app.serializers import UserSerializer
from auth_app.transport import send_pin_code, fetch_recipient
from auth_app.services import add_pin


class UserView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        username = request.GET.get("username", None)
        if username:
            queryset = User.objects.filter(username=username)
            serializer = UserSerializer(queryset, many=True)
        else:
            queryset = User.objects.filter(is_superuser=False)
            serializer = UserSerializer(queryset, many=True)
        response = {"data": serializer.data}
        return Response(response)


class UserInfoView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer([request.user], many=True)
        response = {"data": serializer.data}
        return Response(response)


class PinView(APIView):
    """Отправляет pin для существующего пользователя.
    Пользователь определяется по имени (номеру телефона)
     или адресу электронной почты.
    Порядок получения пользователя определяется в настройках.
    """

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        recipient = request.GET.get("recipient")
        if recipient:
            user = fetch_recipient(recipient)
            if user:
                pin = add_pin(user)
                send_pin_code(pin.pin_code, recipient)
        return Response({"data": None})


class TokenView(APIView):
    """
    Новый токен
    """

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        token = Token.objects.create()
        if token:
            return Response({"data": {"token": token.id}})
        return Response({"data": None})
