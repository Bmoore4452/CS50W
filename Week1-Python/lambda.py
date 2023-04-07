people = [
    {"name": "Brian", "role": "Husband"},
    {"name": "Toya", "role": "Wife"},
    {"name": "Brave", "role": "Son"},
]

# def f(person):
#     return person["name"]

people.sort(key=lambda person: person["name"])

print(people)
