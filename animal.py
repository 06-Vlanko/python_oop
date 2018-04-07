class Animal(object):
    def __init__ (self, name, health):
        self.name = name
        self.health = health
    def walk (self):
        self.health -= 1
        return self
    def run (self):
        self.health -= 5
        return self
    def displayHealth (self):
        print self.health
        return self
# weirdAnimal = Animal ('thingie', 20)
# weirdAnimal.walk().walk().walk().run().run().displayHealth()
class Dog(Animal):
    def __init__ (self, name):
        super(Dog, self).__init__(self, name)
        self.health = 150
    def pet (self):
        self.health += 5
        return self
class Dragon(Animal):
    def __init__(self,name):
        super(Dragon, self).__init__(self, name)
        self.health = 170
    def fly (self):
        self.health -= 10
        return self
    def displayHealth(self):
        super(Dragon, self).displayHealth()
        print 'I am a Dragon'
        return self

weirdAnimal = Animal ('thingie', 20)
#weirdAnimal.pet() generates error 'Animal' object has no attribute 'pet'
#weirdAnimal.displayHealth() shows the established 20
doggie = Dog ('dogo')
doggie.displayHealth()
doggie.pet().displayHealth()
drago = Dragon ('drago')
drago.fly().displayHealth()
