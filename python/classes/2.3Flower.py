# Write a Python class, Flower,
# that has three instance variables of type str, int, and float,
# that respectively represent the name of the flower, its number of petals, and its price.
# Your class must include a constructor method that initializes each variable to an appropriate value,
# and your class should include methods for setting the value of each type, and retrieving the value of each type.

class Flower:

    def __init__(self, name, numPetals, price):
        self.name = name
        self.numPetals = numPetals
        self.price = price

    def display(self):
        print(''.join(['Name: ', self.name, '\nNumber Of Petals: ',
              str(self.numPetals), '\nPrice: ', self.price, ]))

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setNumPetals(self, numPetals):
        self.numPetals = numPetals

    def getNumPetals(self):
        return self.numPetals

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price


flower = Flower('name', 2, '5.99')
flower.display()
print(flower.getNumPetals())
flower.setNumPetals(69)
print(str(flower.getNumPetals()))
