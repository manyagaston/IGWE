from django.db import models

class QuestionType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Type de question"
        verbose_name_plural = "Types des questions"

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Categorie"
        verbose_name_plural = "Categories"

class Difficulty(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Difficulté"
        verbose_name_plural = "Difficultés"

class Question(models.Model):
    question = models.CharField(max_length=500)
    question_type = models.ForeignKey(QuestionType, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    difficulty = models.ForeignKey(Difficulty, on_delete=models.CASCADE)
    correct_answer = models.CharField(max_length=255)
    
    
    def __str__(self):
        return self.question
    
    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"

class Incorrect_answer(models.Model):
    name = models.CharField(max_length=255, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Incorrect answer"
        verbose_name_plural = "Incorrect Answer"


class Personne(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    points = models.IntegerField(default=0)
    
    class Meta:
        verbose_name = "Joueur"
        verbose_name_plural = "Joueurs"
   