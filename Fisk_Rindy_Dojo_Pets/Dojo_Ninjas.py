from Dojo_Pets import Pet

class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        food = self.pet_food
        print(f"Feeding {self.pet.name} {food}!")
        self.pet.eat()
        return self

    def bathe(self):
        self.pet.noise()


treats = ['Bacon', 'Strawberries', 'Spinach', 'Chicken']
pet_food = ['Salad', 'Green Beans']

Layla = Pet("Layla Loo", "Dog", ['silly girl', 'likes to roll on Green Beans'])

Rindy = Ninja('Momma', 'Rindy', Layla, 'treats', 'pet_food')

Rindy.feed();
print(Rindy.pet.name)