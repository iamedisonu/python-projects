# class Vehicle:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Move!")

# class Car(Vehicle):
#   pass

# class Boat(Vehicle):
#   def move(self):
#     print("Sail!")

# class Plane(Vehicle):
#   def move(self):
#     print("Fly!")

# car1 = Car("Ford", "Mustang") #Create a Car object
# boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
# plane1 = Plane("Boeing", "747") #Create a Plane object

# for x in (car1, boat1, plane1):
#   print(x.brand)
#   print(x.model)
# x.move()
 
class India():
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the most widely spoken language of India.")

    def type(self):
        print("India is a developing country.")

class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")

obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()