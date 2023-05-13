
class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 50


    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        self.energy -= 15
        return self

    def noise(self):
        print(self.noise)



# NINJA BONUS: Use modules to separate out the classes into different files.

# SENSEI BONUS: Use Inheritance to create sub classes of pets.

class Mike(Pet):
    def __init__(self, name, type, tricks, size):
        super().__init__(name, type, tricks)
        self.size = size
        self.health = 100
        self.energy = 50


Everleigh = Mike("name", "type", "tricks", "size")
print(Everleigh.type)