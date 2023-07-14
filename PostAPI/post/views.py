from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from PostAPI.post.models import Post
from PostAPI.post.serializers import UserSerializer


# Create your views here.

class RegisterView(generics.GenericApiView):
    serializer_class = UserSerializer

class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)

        if user:
            login(request,user)
            return Response(UserSerializer(user).data)

        return Response({"error": "Wrong Credentials"}, status = status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        logout(request)
        return Response(status=status.HTTP_200_OK)


class PostSerializer:
    pass


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer