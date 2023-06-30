from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .serializers import AuthorSerializer
from .models import Author
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token

# Create your views here.
class Signup(generics.ListCreateAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    authentication_classes = ()

    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save(password=make_password(request.data.get('password')))
            token = Token.objects.create(user=user)
            return Response({'user':serializer.data, 'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Login(generics.GenericAPIView):
    authentication_classes = ()

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            user = Author.objects.get(email=email)
            print(user.password)
        except Author.DoesNotExist:
            return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
        if user.check_password(password):
            token = Token.objects.get(user=user)
            return Response({'user':AuthorSerializer(user).data, 'token':token.key }, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Wrong password'}, status=status.HTTP_401_UNAUTHORIZED)
