class Animal(object):
    def __init__(self,name,health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def display_health(self):
        print (self.health)

dog = Animal("sadie",1000)

dog.walk().walk().walk().run().run().display_health()

