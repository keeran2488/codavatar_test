from rest_framework.generics import CreateAPIView

from account.models import User

from account.serializers import UserRegisterSerializer


class UserCreateView(CreateAPIView):
    serializer_class = UserRegisterSerializer
