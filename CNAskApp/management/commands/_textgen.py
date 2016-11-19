from random import randrange, shuffle
from CNAskApp.management.commands._util import chance


words = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla faucibus ut arcu
at tempor. Mauris faucibus rhoncus blandit. Maecenas vehicula convallis viverra.
Quisque facilisis mi a quam pulvinar rhoncus. Aenean vel sem molestie, tempus sem
eget, gravida leo. Donec vulputate placerat metus, eu faucibus enim venenatis in.
Etiam condimentum, velit non tincidunt lacinia, justo lectus pulvinar diam, sit amet
venenatis libero nunc vitae diam. Nam ut felis a sapien venenatis pretium. Vivamus
ullamcorper massa sed libero ullamcorper iaculis non quis purus. Aliquam auctor dignissim
orci eget sollicitudin. Curabitur urna erat, interdum quis leo eu, commodo ultricies risus.
Ut leo elit, hendrerit eget efficitur in, elementum eget risus. These three QuerySets are
separate. The first is a base QuerySet containing all entries that contain a headline
starting with What. The second is a subset of the first, with an additional criteria
that excludes records whose pub_date is today or in the future. The third is a subset of
the first, with an additional criteria that selects only the records whose pub_date is
today or in the future. The initial QuerySet (q1) is unaffected by the refinement process.
In the examples given so far, we have constructed filters that compare the value of a model
field with a constant. But what if you want to compare the value of a model field with another
field on the same model? Django provides F expressions to allow such comparisons.
Instances of F() act as a reference to a model field within a query. These references
can then be used in query filters to compare the values of two different fields on the
same model instance. For example, to find a list of all blog entries that have had more
comments than pingbacks, we construct an F() object to reference the pingback count,
and use that F() object in the query: The critics have assailed every source of inspiration
save one. To that one we are driven for our moral theme. When we levied upon the masters of
old they gleefully dug up the parallels to our columns. When we strove to set forth real
life they reproached us for trying to imitate Henry George, George Washington, Washington
Irving, and Irving Bacheller. We wrote of the West and the East, and they accused us of
both Jesse and Henry James. We wrote from our heart - and they said something about a
disordered liver. We took a text from Matthew or - er-yes, Deuteronomy, but the preachers
were hammering away at the inspiration idea before we could get into type. So, driven to
the wall, we go for our subject-matter to the reliable, old, moral, unassailable vade
mecum - the unabridged dictionary. For Miss Merriam was lovely and capable. She could take
45 cents out of a $2 bill and refuse an offer of marriage before you could - Next! - lost
your chance - please don't shove. She could keep cool and collected while she collected
your check, give you the correct change, win your heart, indicate the toothpick stand,
and rate you to a quarter of a cent better than Bradstreet could to a thousand in less
time than it takes to pepper an egg with one of Hinkle's casters. There is an old and
dignified allusion to the "fierce light that beats upon a throne." The light that beats
upon the young lady cashier's cage is also something fierce. The other fellow is responsible
for the slang."""

tags = [
    'art', 'innovation', 'cute', 'snootle', 'undertale', 'politics',
    'snootleboops', 'asriel', 'goatbro', 'fluffy', 'economics',
    'usa', 'election', 'trump', 'victory', 'otrageous', 'tempest',
    'python', 'django', 'something', 'primo-victoria', 'sabaton',
    'rock', 'eee-rockkk', 'memes', 'more_memes', 'erp',
    '2good4u', 'gta', 'eggs-with-bacon', 'shakespeare', 'sonet',
    'room', 'lamp', 'national', 'france', 'vietnam', 'flashback',
    'stupid-tag', 'help_me', 'war-thunder', 'guidance', 'best-friend',
    'besties', 'love', 'forever', 'childish', 'childhood', 'mental-issues',
    'important', 'import', 'export', 'growth', 'psycho', 'god', 'godlike',
    'coca-cola', 'dr-pepper', 'fanta', 'sprite', 'thirsty', 'iknowthatfeelbro',
]

words = words.replace('\n', ' ')
words = words.lower().split(" ")


def generate_tags():
    res = []
    for i in range(randrange(3, 7)):
        shuffle(tags)
        res.append('#' + tags[0])
    return ' '.join(res)


def generate(len_min, len_max, is_q=False):
    first = True
    text = []

    for k in range(randrange(len_min, len_max)):
        for i in range(randrange(7, 20)):
            j = randrange(0, len(words))

            try:
                word = ''.join(words[j]).lower().replace(',', '').replace('.', '').\
                    replace('\n', '').replace(':', '').replace('"', '')

                if first:
                    word = word.capitalize()
                first = False
                text.append(word)
            except AttributeError:
                pass

        if chance(50):
            text.append('.')
        elif chance(30):
            text.append('?')
        elif chance(10):
            text.append('!')
        else:
            text.append('...')
        first = True
    if is_q:
        text[len(text) - 1] = '?'

    text = ' '.join(text).replace(' .', '.').replace(' ?', '?').replace(' !', '!').replace(' ...', '...')
    return text


