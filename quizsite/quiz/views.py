from django.shortcuts import render
from rest_framework import viewsets
from .models import Question,Category
from .serializers import QuestionSerializer,CategorySerializer
from rest_framework import generics


class QuestionViewsets(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filterset_fields = ['question_type', 'category','difficulty',]

class CategoryViewsets(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    