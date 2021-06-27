from django.shortcuts import render
from .models import tweep
from rest_framework import viewsets
from tweet.serializers import TweetSerializer


# Create your views here.

class TweetViewSet(viewsets.ModelViewSet):
    serializer_class = TweetSerializer
    queryset = tweep.objects.all()
