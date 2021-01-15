from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework import status
# from dukaan.common.base_view import BaseView
from .serializers import UserSerializer

class CustomAuthToken(ObtainAuthToken):
    base_view = BaseView()
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        if not serializer.is_valid():
            pass
            # return self.base_view.serializer_error_response(
            #     "Authentication failed ", serializer.errors
            # )
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        user_serializer = UserSerializer(user)
        serialized_data = user_serializer.data
        serialized_data["token"] = str(token)
        return Response(serialized_data)