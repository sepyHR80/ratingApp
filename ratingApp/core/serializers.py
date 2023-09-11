from rest_framework import serializers
from .models import Article, Rating

class articleSerializers(serializers.ModelSerializer):
    rating_count = serializers.IntegerField()
    average_rating = serializers.FloatField()
    class Meta:
        model = Article
        fields = ('title', 'description', 'rating_count', 'average_rating')

class ratingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"

