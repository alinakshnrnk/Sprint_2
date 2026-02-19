class PointsForPlace:
    @staticmethod
    def get_points_for_place(place, points=0):
        if place > 100:
            return 'Баллы начисляются только первым 100 участникам'
        elif place < 1:
            return 'Спортсмен не может занять нулевое или отрицательное место'
        else:
            return points + (101 - place)


class PointsForMeters:
    @staticmethod
    def get_points_for_meters(meters, points=0):
        if meters < 0:
            return 'Количество метров не может быть отрицательным'
        else:
            return points + meters * 0.5


class TotalPoints(PointsForPlace, PointsForMeters):
    def get_total_points(self, place, meters):
        points_place = super().get_points_for_place(place)
        points_meters = super().get_points_for_meters(meters)
        total = points_place + points_meters
        return total


points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(-10))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(-10))

total_points = TotalPoints()
print(total_points.get_total_points(place=3, meters=10))