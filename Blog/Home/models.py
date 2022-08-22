from pyexpat import model
from django.db import models

# Create your models here.

class Unit(models.Model):
    unit_text = models.CharField(max_length=200)

class Question(models.Model):
    unit = models.ForeignKey(Unit,on_delete=models.CASCADE)
    question_text = models.CharField(max_length=100)
    result_text = models.CharField(max_length=100)
    result_kanji_text = models.CharField(max_length=100, null=True)
    answer_text = models.CharField(max_length=100, null=True)

class Answer(models.Model):
    ques = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=100)
