from vehicle import *

class MotorBike(Vehicle):

    def __init__(self):
        Vehicle.__init__(self, 2)

    def get_number_of_wheels(self):
      return self.number_of_wheels
        
    def start_engine(self):
        vehicle_start = Vehicle.start_engine(self)
        return vehicle_start + " (I'm a motorbike), HELL YEAH!"
