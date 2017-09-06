from animal import Animal

class Dog(Animal):
    def __init__(self):
        super(Dog, self).__init__("dog",150)

    def pet(self):
        self.health += 5
        return self

sadie = Dog()

sadie.walk().walk().walk().run().run().pet().display_health()
