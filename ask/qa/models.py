# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class QuestionManager(models.Manager):
	def new():
		pass
	def popular():
		pass

class Question(models.Model):
	objects = QuestionManager()
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add=True)
	rating = models.BigIntegerField(default=1)
	author = models.ForeignKey(User, related_name='question_user', blank=True, null=True)
	likes = models.ManyToManyField(User, related_name='%(app_label)s_%(class)s_related', blank=True)


class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add=True)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	author = models.OneToOneField(User, on_delete=models.CASCADE)


		

