from django.shortcuts import render
from rest_framework import viewsets
from .models import Question
from .serializers import QuestionSerializer
from rest_framework import generics
from .models import Personne
from .serializers import PersonneSerializer

class QuestionViewsets(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filterset_fields = ['question_type', 'category','difficulty',]

class PersonneCreateView(generics.CreateAPIView):
    queryset = Personne.objects.all()
    serializer_class = PersonneSerializer