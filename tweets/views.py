from django.shortcuts import render

# Create your views here.
from .models import User, Tweets
from rest_framework import viewsets

# from rest_framework import permissions
from .serializer import UserSerializer, TweetsSerializer

# takes serialized data and renders it
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated] view is limited to if person is signed in or not


class TweetsViewSet(viewsets.ModelViewSet):
    queryset = Tweets.objects.all()
    serializer_class = TweetsSerializer
