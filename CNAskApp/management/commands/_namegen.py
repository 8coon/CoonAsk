from CNAskApp.management.commands._util import chance
from random import shuffle, randrange


first_names = [
    'James', 'David', 'Christopher', 'George' 'Ronald',
    'John', 'Richard', 'Daniel', 'Kenneth', 'Anthony',
    'Robert', 'Charles', 'Paul', 'Steven', 'Kevin',
    'Michael', 'Joseph', 'Mark', 'Edward', 'Jason',
    'William', 'Thomas', 'Donald', 'Brian', 'Jeff',
]

last_names = [
    'Price', 'Bennett', 'Wood', 'Barnes', 'Ross', 'Henderson',
    'Coleman', 'Jenkins', 'Perry', 'Powell', 'Long', 'Patterson',
    'Hughes', 'Flores', 'Washington', 'Butler', 'Simmons', 'Foster',
    'Gonzales', 'Bryant', 'Alexander', 'Russell', 'Collins', 'Thompson',
]


emails = [
    '@gmail.com', '@mail.ru', '@icloud.com'
]


def generate_email(name):
    shuffle(emails)
    return name + emails[0]


def generate():
    shuffle(first_names)
    shuffle(last_names)
    first_name = first_names[0]
    last_name = last_names[0]
    username = first_name

    if chance(40):
        username = username.lower()

    if chance(40):
        if chance(50):
            username += "_"
        username += last_name

    username += str(randrange(1970, 2005))

    if chance(85):
        return username, first_name, last_name, generate_email(username)
    return username, "", "", generate_email(username)
