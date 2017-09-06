from animal import Animal
from dog import Dog

class Dragon(Animal):
    def __init__(self):
        super(Dragon,self).__init__("dragon",170)

    def fly(self):
        self.health -= 10

    def display_health(self):
        super(Dragon,self).display_health()
        print ("I am a Dragon")

brownie = Animal("cat",9)
brownie.pet()
brownie.fly()
brownie.display_health()

sade = Dog()
sade.fly()
