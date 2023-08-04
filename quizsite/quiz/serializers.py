from rest_framework import serializers
from rest_framework.fields import ListField
from .models import Question,Personne
   

class QuestionSerializer(serializers.ModelSerializer):
    questions = serializers.CharField(source="question", read_only=True)
    correct_answers = serializers.CharField(source="correct_answer", read_only=True)
    categorys = serializers.CharField(source="category", read_only=True)
    type = serializers.CharField(source="question_type", read_only=True)
    #incorrect_answer = IncorrectAnswerSerializer(many=True, read_only=True)
    difficulty_name = serializers.CharField(source="difficulty", read_only=True)
    incorrect_answer = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Question
        fields = ('questions', 'type', 'categorys','difficulty_name', 'correct_answers', 'incorrect_answer',)
        

class PersonneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personne
        fields = ['name', 'password', 'points']