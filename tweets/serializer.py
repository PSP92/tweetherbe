from rest_framework import serializers
from .models import User, Tweets


class UserSerializer(serializers.ModelSerializer):
    # Meta class specific to this ^ serializer definies everything that goes throughout the  overall serializer class
    class Meta:
        model = User
        fields = ["id", "name", "email"]


class TweetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweets
        fields = ["id", "body", "img", "likes", "tags"]
