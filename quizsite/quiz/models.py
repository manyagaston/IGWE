from django.db import models

class QuestionType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Difficulty(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class IncorrectAnswer(models.Model):
    reponse = models.TextField()
    
   
    def __str__(self):
        return self.reponse


class Question(models.Model):
    question = models.CharField(max_length=255)
    question_type = models.ForeignKey(QuestionType, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    difficulty = models.ForeignKey(Difficulty, on_delete=models.CASCADE)
    incorrect_answer = models.ManyToManyField(IncorrectAnswer, blank=True)
    correct_answer = models.CharField(max_length=255)
    

    def __str__(self):
        return self.question

class Personne(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    points = models.IntegerField(default=0)