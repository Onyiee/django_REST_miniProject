from rest_framework import serializers
from .models import tweep


class TweetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = tweep
        fields = ['tweep', 'date_created']
