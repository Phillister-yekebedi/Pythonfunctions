# 2) Create a files in the classes directory car.py. Define the following class
# in each module respectively. 

# Each class should have one class attribute and three instance variables.

# class Car:
#     make = "Mercedes"
#     Model = "S_class"
#     colour = "maroon"

    
class Car:
   steering_wheel = 1

def __init__(self, make, model, colour):
        self.make = make
        self.model = model
        self.colour = colour

def details(self):
        return f"This is a {self.make} {self.model} {self.colour} with steering wheel."
