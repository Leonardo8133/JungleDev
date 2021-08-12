from api.models import User, Article, Author
import random


""" 
    Testing Purpose Only

    Pre populate the database, making the testing process easier

"""


user, _ = User.objects.get_or_create(
        username = 'admin',
        email = 'admin@admin.com',
        is_superuser = True,
        is_staff = True)

user.set_password("admin")
user.save()

categories = [
            "Action",
            "Adventure",
            "Classics",
            "Comic",
            "Detective",
            "Mystery",
            "Fantasy"
            ]

authors = [ "Nathan B. Schreiner",
            "Tameka A. Cote",
            "Chas K. Robbins",
            "Timothy S. Belgrave",
            "Brooke D. Dessert",
            "Ada J. Milligan",
            "Betty R. Hopson"
            ]

titles = [
"Five Minutes in China",
"Forty Winks at the Pyramids​",
"Abernethy on the Constitution",
"A Carpenter’s Bench of Bishops",
"Toot’s Universal Letter-Writer",
"Orson’s Art of Etiquette​",
"Downeaster’s Complete Calculator",
"History of the Middling Ages",
"Jonah’s Account of the Whale",
"Captain Parry’s Virtues of Cold Tar",
"Kant’s Ancient Humbugs​",
"Bowwowdom. A Poem",
"The Quarrelly Review",
"The Gunpowder Magazine",
"Steele. By the Author of ‘Ion’",
"The Art of Cutting the Teeth",
"Matthew’s Nursery Songs",
"Paxton’s Bloomers",
"On the Use of Mercury by the Ancient Poets",
"Drowsy’s Recollections of Nothing​",
"Heavyside’s Conversations with Nobody",
"Commonplace Book of the Oldest Inhabitant",
]

body = "This is the First paragraph    This is the Second paragraph   This is the Third paragraph, where the book ends"

authors_object_list = []
for author in authors:
    authors_object_list.append(Author.objects.get_or_create(name = author)[0])


for x in range(20):
    data = {"title": random.choice(titles), "category": random.choice(categories), "author": random.choice(authors_object_list), "summary":"This is a fake book", "text": body}
    if Article.objects.filter(title = data["title"]).exists():
        continue
    Article.objects.create(**data)
