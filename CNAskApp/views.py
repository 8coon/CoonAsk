from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth import login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required
from CNAskApp.models import CNTag, CNProfile, CNQuestion
from CNAskApp.forms import CNSignupForm, CNLoginForm, CNProfileForm, CNAskForm, CNAnswerForm
from CNAskApp.feed import CNPostSorting, get_questions, get_paginator


def mixin(request, d, **kwargs):
    offset = kwargs.get("offset", 0)
    count = kwargs.get("count", 0)
    final = {
        "popular_tags": CNTag.objects.top(),
        "best_members": CNProfile.objects.top(),
        "profile": CNProfile.objects.profile(request.user),
        "paginator": get_paginator(offset, count)
    }
    final.update(d)
    return final


def index(request):
    return most(request, "recent")


def login(request):
    form = CNLoginForm()

    if request.method == "POST":
        form = CNLoginForm(request.POST)

        if form.is_valid():
            django_login(request, form.user)
            return HttpResponseRedirect("/")

    return render(request, "login.html", mixin(request, {
        "form": form,
    }))


def logout(request):
    django_logout(request)
    return HttpResponseRedirect("/")


def signup(request):
    form = CNSignupForm()

    if request.method == "POST":
        form = CNSignupForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/login/#signup_success")

    return render(request, "signup.html", mixin(request, {
        "form": form,
    }))


def profile(request, name):
    viewing = CNProfile.objects.profile_str(name)
    form = CNProfileForm.load(viewing)
    success = None

    if (request.method == "POST") and (viewing.django_user == request.user):
        form = CNProfileForm(request.POST)

        if form.is_valid():
            form.save(viewing)
            success = "Profile data successfully saved!"

    return render(request, "profile.html", mixin(request, {
        "viewing": viewing,
        "form": form,
        "success": success,
    }))


@login_required
def ask(request):
    form = CNAskForm()

    if request.user.is_authenticated() and request.method == "POST":
        form = CNAskForm(request.POST)

        if form.is_valid():
            q_id = form.save(CNProfile.objects.get(django_user=request.user))
            return HttpResponseRedirect("/question/" + str(q_id))

    return render(request, "ask.html", mixin(request, {
        "form": form,
    }))


def question(request, id):
    question = get_object_or_404(CNQuestion, pk=id)

    form = CNAnswerForm()
    success = None

    if request.method == "POST":
        form = CNAnswerForm(request.POST)

        if form.is_valid():
            form.save(
                author=CNProfile.objects.get(django_user=request.user),
                question=question,
            )
            success = "Your answer has been saved!"

    return render(request, "question.html", mixin(request, {
        "question": question,
        "success": success,
        "form": form,
    }))


def generic_feed(request, category, username=None, tag=None):
    cats = CNPostSorting.categories()
    offset = int(request.GET.get("offset", 0))
    questions, arg, count = get_questions(category, offset, username, tag)

    return render(request, "feed.html", mixin(request, {
        "questions": questions,
        "category": CNPostSorting.categories_dict()[category]["title"].replace("$ARG$", arg),
        "categories": cats,
    }, offset=offset, count=count))


def most(request, cat_arg):
    return generic_feed(request, CNPostSorting.find_cat("most", cat_arg)["name"])


def unanswered(request):
    return generic_feed(request, CNPostSorting.find_cat("unanswered", None)["name"])


def questions_of(request, cat_arg):
    return generic_feed(request,
                        CNPostSorting.find_cat("questions-of", None)["name"],
                        username=cat_arg)


def questions_tagged_with(request, cat_arg):
    return generic_feed(request,
                        CNPostSorting.find_cat("questions-tagged-with", None)["name"],
                        tag=cat_arg)


def search(request):
    pass
