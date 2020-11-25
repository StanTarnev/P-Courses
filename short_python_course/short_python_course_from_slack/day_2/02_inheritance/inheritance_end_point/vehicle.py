class Vehicle:

    def __init__(self, number_of_wheels):
        self.number_of_wheels = number_of_wheels

    def get_number_of_wheels(self):
        return self.number_of_wheels

    def start_engine(self):
        return "Vrrmm"