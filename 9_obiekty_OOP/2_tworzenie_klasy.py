class Cat:
    species = "mammal"
    number_of_legs = 4

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("Meow ~" + self.name)


puszek = Cat("Puszek", 2)
mruczek = Cat("Mruczek", 4)
garfield = Cat("Garfield", 10)

print("gatunek Puszka:", puszek.species)  # atrybut obiektu
print("kot ma:", puszek.number_of_legs, "łap")

puszek.number_of_legs = 3
print("kot ma:", puszek.number_of_legs, "łap")
print(f"{puszek.name} ma {puszek.number_of_legs} łap")
print(f"{mruczek.name} ma {mruczek.number_of_legs} łap")

print("imię Puszka:", puszek.name)  # atrybut obiektu
puszek.speak()  # wywołanie metody
