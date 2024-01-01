movies = [
{'title': 'Ojciec chrzestny', 'director': 'Francis Ford Coppola', 'year': 1972},
{'title': 'Skazani na Shawshank', 'director': 'Frank Darabont', 'year': 1994},
{'title': 'Szeregowiec Ryan', 'director': 'Steven Spielberg', 'year': 1998},
{'title': 'Obywatel Kane', 'director': 'Orson Welles', 'year': 1998},
{'title': 'Casablanca', 'director': 'Michael Curtiz', 'year': 1942},
{'title': 'Titanic', 'director': 'James Cameron', 'year': 1997},
{'title': 'Lista Schindlera', 'director': 'Steven Spielberg', 'year': 1993}
]

updated = []

for movie in movies:
    if movie['director'] != 'Steven Spielberg':
        updated.append(movie)

print(updated)

