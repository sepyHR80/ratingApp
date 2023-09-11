from rest_framework import serializers
from .models import Article, Rating

class articleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"

class ratingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"

