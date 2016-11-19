from django.shortcuts import get_object_or_404, Http404
from CNAskApp.models import CNQuestion, CNTag, CNProfile


paginator_block_size = 10


class CNPostSorting:
    @staticmethod
    def categories():
        cats = [
            {"name": "new", "url_name": "new", "url": "most", "arg": "recent",
                "title": "Newest", "hidden": False},

            {"name": "most_answered", "url": "most", "arg": "answered",
                "title": "Most Answered", "hidden": False},

            {"name": "top_rated", "url": "most", "arg": "rated",
                "title": "Most Rated", "hidden": False},

            {"name": "new_unanswered", "url": "unanswered", "arg": None,
                "title": "Unanswered", "hidden": False},

            {"name": "users", "url": "questions-of", "arg": False,
                "title": "Questions of $ARG$", "hidden": True},

            {"name": "tagged", "url": "questions-tagged-with", "arg": False,
                "title": "Questions tagged with #$ARG$", "hidden": True},
        ]

        for cat in cats:
            cat["python_name"] = cat["url"].replace("-", "_")
        return cats

    @staticmethod
    def categories_dict():
        categories = CNPostSorting.categories()
        res = {}

        for cat in categories:
            res[cat["name"]] = cat
        return res

    @staticmethod
    def find_cat(url, arg):
        for cat in CNPostSorting.categories():
            if (cat["url"] == url) and ((cat["arg"] == arg) or (cat["arg"] == False)):
                return cat
        raise Http404("Category not found")


def get_questions(category, offset, username=None, tag=None):
    questions = None
    arg = ""

    if category == "new":
        questions = CNQuestion.objects.order_by("-timestamp")
    elif category == "most_answered":
        questions = CNQuestion.objects.order_by("-answers_count")
    elif category == "top_rated":
        questions = CNQuestion.objects.order_by("-rating")
    elif category == "new_unanswered":
        questions = CNQuestion.objects.filter(answers_count=0).order_by("-timestamp")
    elif category == "users":
        arg = username
        user = CNProfile.objects.profile_str(username)
        questions = CNQuestion.objects.filter(author=user).order_by("-timestamp")
    elif category == "tagged":
        arg = tag
        tag = get_object_or_404(CNTag, name=tag)
        questions = tag.questions.all().order_by("-timestamp")

    count = questions.count()

    if (offset < 0) or (offset > count + paginator_block_size):
        raise Http404("Wrong offset")

    questions = questions[offset:offset + paginator_block_size]
    return questions, arg, count


def get_paginator(offset, count):
    def expand(arr):
        res = []
        for el in arr:
            res.append({
                "selected": "selected" if el == current else None,
                "offset": el * paginator_block_size - paginator_block_size,
                "index": el})
        return res

    def simplify():
        new_first = []
        for el in range(pages):
            new_first.append(el + 1)
        return new_first, [], [], False, False

    pages = count // paginator_block_size + 1
    current = offset // paginator_block_size + 1

    first = [1, 2]
    last = [pages - 1, pages]
    middle = []
    first_dots = False
    last_dots = True

    if current == 3:
        first.append(current)
        first.append(current + 1)
    elif current == 2:
        first.append(current + 1)
    elif current == pages - 2:
        last = [current - 1] + [current] + last
    elif current == pages - 1:
        last = [current - 1] + last
    elif 3 < current < pages - 2:
        first_dots = True
        rounded = current // 2 * 2
        middle = [i for i in range(rounded - 1, rounded + 3)]

    if pages < 9:
        first, middle, last, first_dots, last_dots = simplify()

    return {
        "first": expand(first),
        "middle": expand(middle),
        "last": expand(last),
        "first_dots": first_dots,
        "last_dots": last_dots,
    }


