class Movies:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)


class Comedy(Movies):
    def show(self):
     return f'Комедии: {self.movies}'


class Drama(Movies):
    def show(self):
        return f'Драмы: {self.movies}'


c = Comedy()
c.add_movie('Большой куш')
a = Drama()
a.add_movie('Оружейный барон')

print(c.show())
print(a.show())