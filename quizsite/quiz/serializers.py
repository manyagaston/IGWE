from rest_framework import serializers
from rest_framework.fields import ListField
from .models import Question,Personne,Incorrect_answer

class Incorrect_answerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incorrect_answer
        fields = ('name', )


class QuestionSerializer(serializers.ModelSerializer):
    questions = serializers.CharField(source="question", read_only=True)
    correct_answers = serializers.CharField(source="correct_answer", read_only=True)
    categorys = serializers.CharField(source="category", read_only=True)
    type = serializers.CharField(source="question_type", read_only=True)
    incorrect_answers = serializers.SerializerMethodField()
    difficultys = serializers.CharField(source="difficulty", read_only=True)
   
        
    class Meta:
        model = Question
        fields = ('questions', 'type', 'categorys','difficultys', 'correct_answers', 'incorrect_answers', )
        
 
    
    def get_incorrect_answers(self, question):
        incorrect_answers = Incorrect_answer.objects.filter(question=question)
        return [book.name for book in incorrect_answers]



class PersonneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personne
        fields = ['name', 'password', 'points']
 