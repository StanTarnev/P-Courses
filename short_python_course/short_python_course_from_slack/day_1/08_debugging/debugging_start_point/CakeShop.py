class CakeShop():
    def __init__(self, cakes):
        self.cakes = cakes

    def get_average_rating(self):
        ratings = []

        for cake in self.cakes:
            ratings.append(cake.rating)

            ratings_total = sum(ratings)

            number_of_cakes = len(self.cakes)

            average = ratings_total / number_of_cakes

            return average
