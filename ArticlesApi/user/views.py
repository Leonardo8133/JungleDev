from rest_framework.generics import CreateAPIView
from user.models import User
from user.serializers import CreateUserSerializer


# Create your views here.
class CreateUserView(CreateAPIView):
    """  Register Only Endpoint """
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer