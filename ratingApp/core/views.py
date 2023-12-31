from django.shortcuts import render
from .models import Article, Rating
from .serializers import articleSerializers, ratingSerializers
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Avg, Count


class ArticleListView(ListAPIView):
    queryset = Article.objects.annotate(
        rating_count=Count('rating'),
        average_rating=Avg('rating__rating')
    )
    serializer_class = articleSerializers

class ArticleRateView(CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = ratingSerializers

    def create(self, request, *args, **kwargs):
        article = self.request.data.get("article")
        rate = self.request.data.get("rating")
        user = self.request.user

        try :
            obj_1 = Rating.objects.get(user = user, article_id = article)
            obj_1.rating = rate
            obj_1.save()

        except Rating.DoesNotExist:
            obj_1 = Rating(user = user, article_id = article,rating = rate)
            obj_1.save()
        
        return Response({'message': 'Rating submitted'}, status=status.HTTP_201_CREATED)
            
