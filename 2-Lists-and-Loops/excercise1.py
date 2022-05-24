star_wars_movies = [
    ["The Phantom Menace", "Attack of the Clones", "Revenge of the Sith"],
    ["A New Hope", "The Empire Strikes Back", "Return of the Jedi"],
    ["The Force Awakens", "The Last Jedi", "The Rise of Skywalker"],
]

trilogy = int(input("Please enter a number of the trilogy: "))
film = int(input("Please enter a number of the film in this trilogy: "))

print(star_wars_movies[trilogy-1][film-1])
