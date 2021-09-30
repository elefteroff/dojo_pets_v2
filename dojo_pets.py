class Ninja:

    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()
        print(f"After a walk {kentaro.pet.name}'s health is now {kentaro.pet.health}")
        return self

    def feed(self):
        self.pet.eat()
        print(f"After eating {kentaro.pet.name}'s energy is now {kentaro.pet.energy}")
        print(f"After eating {kentaro.pet.name}'s health is now {kentaro.pet.health}")
        return self

    def bathe(self):
        self.pet.noise()
        return self

class Pet:

    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = 50
        self.health = 80

    def sleep(self):
        self.energy *= 1.25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        return self

    def noise(self):
        print(f"Durring a bath {kentaro.pet.name} says 'Whoof'")

kentaro = Ninja("Kentaro", "Sakagawa", "Doggie Biscuits", "Canned Dog Food", "Dog")
fletch = Pet("Fletch", "Dog", "Rolls Over")

kentaro.pet = fletch

kentaro.walk()
kentaro.feed()
kentaro.bathe()

