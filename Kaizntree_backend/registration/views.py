from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
# Create your views here.


@api_view(['POST'])
def login(request):
    data = request.data

    serializer = LoginSerializer(data=data)
    if serializer.is_valid():
        user = authenticate(
            username=serializer.data['username'], password=serializer.data['password'])
        if not user:
            print('login err')
            return Response({"message": "Invalid credentials!", "status": "false"}, status=status.HTTP_400_BAD_REQUEST)
        token = Token.objects.get_or_create(user=user)
        return Response({"message": "success", "token": str(token[0])}, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def signup(request):
    data = request.data
    serializer = SignupSerializer(data=data)
    if serializer.is_valid():
        user = serializer.save()
        token = Token.objects.get_or_create(user=user)

        return Response({"message": "User successfully logged in", "token": str(token[0])}, status=status.HTTP_201_CREATED)
    else:
        return Response({"message": serializer.errors, "status": "false"}, status=status.HTTP_400_BAD_REQUEST)
