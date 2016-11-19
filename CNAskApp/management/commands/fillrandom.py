from django.core.management.base import BaseCommand
from random import randrange, shuffle
from CNAskApp.forms import CNSignupForm, CNAskForm, CNAnswerForm, CNProfileForm
from CNAskApp.models import CNProfile, CNQuestion
from CNAskApp.management.commands import _namegen, _textgen


class Command(BaseCommand):
    help = "Generates things"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        usernames = []

        for i in range(30):
            username, first_name, last_name, email = _namegen.generate()

            try:
                form = CNSignupForm(data={
                    "login": username,
                    "email": email,
                    "password": "changeme",
                    "password_again": "changeme",
                })

                if form.is_valid():
                    form.save()

                    if first_name != "":
                        form = CNProfileForm(data={
                            "first_name": first_name,
                            "last_name": last_name,
                            "status": _textgen.generate(1, 3),
                            "info": _textgen.generate(20, 30),
                        })

                        if form.is_valid():
                            profile = form.save(CNProfile.objects.profile_str(username))
                            profile.avatar = randrange(1, 13)
                            profile.save()
                    usernames.append(username)
            except Exception:
                pass

        questions = []

        for j in range(len(usernames)):
            for i in range(randrange(5, 40)):
                try:
                    shuffle(usernames)
                    username = usernames[0]

                    form = CNAskForm(data={
                        "title": _textgen.generate(1, 2, True),
                        "text": _textgen.generate(3, 7),
                        "tags": _textgen.generate_tags(),
                    })

                    if form.is_valid():
                        pk = form.save(CNProfile.objects.profile_str(username))

                        question = CNQuestion.objects.get(pk=pk)
                        question.rating = randrange(-20, 20)
                        question.save()

                        questions.append(pk)
                except Exception:
                    pass

        for username in usernames:
            for i in range(randrange(5, 15)):
                shuffle(questions)
                question = CNQuestion.objects.get(pk=questions[0])

                form = CNAnswerForm(data={
                    "text": _textgen.generate(3, 7),
                })

                if form.is_valid():
                    form.save(CNProfile.objects.profile_str(username), question)

