from django.contrib import admin
from .models import Question,IncorrectAnswer,Category,QuestionType,Difficulty,Personne

@admin.register(Category,QuestionType,Difficulty)
class QuizAdmin(admin.ModelAdmin):
    pass

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'question_type', 'category','difficulty', 'correct_answer',)
    list_filter = ('question_type', 'category','difficulty',)
    search_fields = ('category',)

admin.site.register(Question, QuestionAdmin)

class IncorrectAnswerAdmin(admin.ModelAdmin):
    list_display = ('reponse',)
    list_filter = ('reponse',)
    search_fields = ('reponse',)

admin.site.register(IncorrectAnswer, IncorrectAnswerAdmin)

class PersonneAdmin(admin.ModelAdmin):
    list_display = ('name','password',)
    list_filter = ('name',)
    search_fields = ('points',)

admin.site.register(Personne, PersonneAdmin)