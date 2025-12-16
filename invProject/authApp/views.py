from rest_framework.generics import CreateAPIView
from .serializer import RegisterSerializer

class RegisterAPIView(CreateAPIView):
    serializer_class = RegisterSerializer
