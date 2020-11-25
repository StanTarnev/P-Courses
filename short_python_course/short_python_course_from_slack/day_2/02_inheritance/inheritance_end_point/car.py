from vehicle import *

class Car(Vehicle):
    def __init__(self, model):
        Vehicle.__init__(self, 4)
        self.model = model

    def get_model(self):
        return self.model
