from rest_framework.viewsets import ModelViewSet

from exam.models import User
from exam.serializers import UserSerializer


class UserView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
