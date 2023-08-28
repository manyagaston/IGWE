from django.shortcuts import render
from rest_framework import viewsets
from .models import Question, Personne,Incorrect_answer
from .serializers import QuestionSerializer,PersonneSerializer
from rest_framework import generics


class QuestionViewsets(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filterset_fields = ['question_type', 'category','difficulty',]

class PersonneCreateView(generics.CreateAPIView):
    queryset = Personne.objects.all()
    serializer_class = PersonneSerializer
 