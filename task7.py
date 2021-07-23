users_list = [
    ('Александр', 'ru'),
    ('James', 'us'),
    ('Daniella', 'es'),
    ('Someone', 'unknown country'),
]

greetings = {
    "ru": "Привет, {}!",
    "us": "Hello, {}!",
    "es": "Hola, {}!",
    "unknown country": "Hello, {}, but I do not know where are you from!"
}


def choose_greeting(tup):
    """
    Chooses correct greeting for each language and returns a greeting string
    """
    name, lang = tup
    greeting = greetings.get(lang, greetings["unknown country"])
    return greeting.format(name)


users_greetings = map(choose_greeting, users_list)
for greeting in users_greetings:
    print(greeting)
