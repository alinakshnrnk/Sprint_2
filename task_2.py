class Movies:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)


class Comedy(Movies):
    def show(self, movie):
     super().add_movie(movie)
     return print(f'Комедии: {self.movies}')


class Drama(Movies):
    def show(self, movie):
     super().add_movie(movie)
     return print(f'Драмы: {self.movies}')


c = Comedy()
c.show('Большой куш')
a = Drama()
a.show('Оружейный барон')