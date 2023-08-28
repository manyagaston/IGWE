from django.contrib import admin
from django.db import models
from django.contrib.admin.widgets import FilteredSelectMultiple
from django import forms
from .models import Question,Category,QuestionType,Difficulty,Personne,Incorrect_answer

@admin.register(Difficulty)
class QuizAdmin(admin.ModelAdmin):
    pass
    
class ModeleInline(admin.TabularInline):
    model = Question
    extra = 0
    

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [ModeleInline]
   
   
@admin.register(QuestionType)
class QuestionType(admin.ModelAdmin):
    inlines = [ModeleInline]
    list_per_page = 5

    

class ResponseInline(admin.TabularInline):
    model = Incorrect_answer
    extra = 1


    
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ResponseInline]
    list_display = ('question', 'question_type', 'difficulty','category', 'correct_answer',)
    list_filter = ('question_type', 'category',)
    search_fields = ('category',)
    list_per_page = 5

admin.site.register(Question, QuestionAdmin)


#class PersonneAdmin(admin.ModelAdmin):
 #   list_display = ('name','password',)
#    list_filter = ('name',)
 #   search_fields = ('points',)
 #   list_per_page = 10

#admin.site.register(Personne, PersonneAdmin)