from django.db import models
from django.core.validators import *
from django.contrib.auth.models import User
from bs4 import BeautifulSoup
from CNAskApp.managers import CNProfileManager, CNQuestionManager, CNAnswerManager, CNTagManager


class CNProfile(models.Model):
    objects = CNProfileManager()

    django_user = models.OneToOneField(User)
    avatar = models.IntegerField(default=0)
    status = models.TextField(max_length=255, default="")
    info = models.TextField(max_length=2000, default="")
    questions_count = models.IntegerField(default=0)
    answers_count = models.IntegerField(default=0)


class CNQuestion(models.Model):
    objects = CNQuestionManager()

    title = models.TextField(max_length=100, default="")
    author = models.ForeignKey("CNProfile")
    full_text = models.TextField(max_length=10000)
    short_text = models.TextField(max_length=300)
    attachments = models.CharField(validators=[validate_comma_separated_integer_list], max_length=255,
                                   default="")
    rating = models.IntegerField(default=0)
    answers_count = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)

    @staticmethod
    def shorten(text):
        short = BeautifulSoup(text, "html5lib").get_text()

        if len(short) > 295:
            short = short[:295]
            short += "..."
        return short

    def get_tags(self):
        return self.cntag_set.all()

    def get_answers(self):
        return CNQuestion.objects.get_answers(self, CNAnswer)


class CNAnswer(models.Model):
    objects = CNAnswerManager()

    question = models.ForeignKey("CNQuestion")
    author = models.ForeignKey("CNProfile")
    is_best = models.BooleanField(default=False)
    full_text = models.TextField(max_length=10000)
    attachments = models.CharField(validators=[validate_comma_separated_integer_list], max_length=255,
                                   default="")
    rating = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)


class CNTag(models.Model):
    objects = CNTagManager()

    questions = models.ManyToManyField("CNQuestion")
    name = models.CharField(max_length=255)
    count = models.IntegerField(default=0)


class CNLike(models.Model):
    answer = models.ForeignKey("CNAnswer", null=True, default=None)
    profile = models.ForeignKey("CNProfile")
