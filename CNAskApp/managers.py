from django.shortcuts import get_object_or_404
from django.db.models import Manager
from django.contrib.auth.models import User, AnonymousUser


class CNProfileManager(Manager):
    def top(self):
        users = self.order_by("-questions_count")[:5]
        return users

    def profile_str(self, username):
        user = get_object_or_404(User, username=username)
        return self.profile(user)

    def profile(self, user):
        if user.is_anonymous():
            return None
        return self.get(django_user=user)

    def has(self, login):
        exists = True

        try:
            User.objects.get(username=login)
        except User.DoesNotExist:
            exists = False

        return exists


class CNQuestionManager(Manager):
    def get_answers(self, question, ans_obj):
        return ans_obj.objects.filter(question=question).order_by("timestamp")


class CNAnswerManager(Manager):
    pass


class CNTagManager(Manager):
    def top(self):
        tags = self.order_by("-count")
        tags = tags[0:20]

        return tags

    def inc(self, obj, tag_name, question):
        try:
            tag = self.get(name=tag_name)
        except obj.DoesNotExist:
            tag = obj(name=tag_name)
            tag.save()

        tag.count += 1
        tag.questions.add(question)
        tag.save()
        return tag
