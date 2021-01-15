from .models.user_model import CustomUser

from .base_serializer import BaseSerializer


class UserSerializer(BaseSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "login_method",
            "email",
        ]


class UserAttributesSerializer(BaseSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "phone",
        ]


class UserBasicInfoSerializer(BaseSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "id",
            "first_name",
            "last_name",
        ]
