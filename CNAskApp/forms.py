from django.forms import Form, CharField, EmailField, ValidationError, FileField
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from re import sub
from CNAskApp.models import CNProfile, CNQuestion, CNTag, CNAnswer


password_help_text = "8 to 30 characters, one digit, one lower- and one uppercase"


class CNSignupForm(Form):
    login = CharField(label="Login", initial="", max_length=30, min_length=4)
    email = EmailField(label="Email", initial="", max_length=30, min_length=4)
    password = CharField(label="Password", initial="",
                         help_text=password_help_text, max_length=30, min_length=8)
    password_again = CharField(label="", help_text="Repeat password", initial="",
                               max_length=30, min_length=8)

    def clean(self):
        if self.cleaned_data.get("password") != self.cleaned_data.get("password_again"):
            raise ValidationError("Passwords do not match!")
        return self.cleaned_data

    def clean_login(self):
        if CNProfile.objects.has(self.cleaned_data["login"]):
            raise ValidationError("This login has already been used!")
        return self.cleaned_data["login"]

    def save(self):
        user = User.objects.create_user(self.cleaned_data["login"],
                                        self.cleaned_data["email"],
                                        self.cleaned_data["password"])
        profile = CNProfile(django_user=user)
        profile.save()
        return profile


class CNLoginForm(Form):
    login = CharField(label="Login", initial="", max_length=30, min_length=4)
    password = CharField(label="Password", initial="", max_length=30, min_length=8)
    user = None

    def clean(self):
        login = self.cleaned_data.get("login")
        password = self.cleaned_data.get("password")
        user = authenticate(username=login, password=password)

        if user is None:
            raise ValidationError("Wrong login or password, try again!")
        self.user = user
        return self.cleaned_data


class CNProfileForm(Form):
    avatar_file = FileField(label="Avatar", allow_empty_file=True, required=False)
    first_name = CharField(help_text="First name", max_length=30, required=False)
    last_name = CharField(help_text="Last name", max_length=30, required=False)
    status = CharField(help_text="Write something short about yourself", max_length=255,
                       required=False)
    info = CharField(max_length=2000, required=False)

    @staticmethod
    def load(profile):
        form = CNProfileForm(initial={
            "first_name": profile.django_user.first_name,
            "last_name": profile.django_user.last_name,
            "status": profile.status,
            "info": profile.info,
        })
        return form

    def save(self, profile):
        profile.django_user.first_name = self.cleaned_data["first_name"]
        profile.django_user.last_name = self.cleaned_data["last_name"]
        profile.django_user.save()

        profile.status = self.cleaned_data["status"]
        profile.info = self.cleaned_data["info"]
        profile.save()
        return profile


class CNAskForm(Form):
    title = CharField(label="Title", initial="",
                      help_text="Give a brief description to your question",
                      max_length=100, min_length=8)
    text = CharField(label="Text", initial="",
                     help_text="Maximum 10000 characters",
                     max_length=10000, required=False)
    tags = CharField(label="Tags", initial="",
                     help_text="#elections #usa #trump",
                     max_length=100)

    def save(self, author):
        question = CNQuestion(title=self.cleaned_data["title"], author=author,
                              full_text=self.cleaned_data["text"],
                              short_text=CNQuestion.shorten(self.cleaned_data["text"]))
        question.save()

        author.questions_count += 1
        author.save()

        tags = self.cleaned_data["tags"].replace(",", " ")
        tags = sub(r"[^\w\s]", "", tags)
        tags = sub(r"\s+", " ", tags)
        tags = tags.lower()
        tags = tags.split(" ")

        for tag in tags:
            CNTag.objects.inc(CNTag, tag, question)

        return question.pk


class CNAnswerForm(Form):
    text = CharField(label="Your Answer", initial="",
                     help_text="Maximum 10000 characters, please be polite and gentle...",
                     max_length=10000, required=True)

    def save(self, author, question):
        answer = CNAnswer(question=question, author=author, full_text=self.cleaned_data["text"])
        answer.save()

        author.answers_count += 1
        author.save()

        question.answers_count += 1
        question.save()


