class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

class Mammal(Animal):
    def give_birth(self):
        print(f"{self.name} gives birth to live young")

class Bird(Animal):
    def lay_eggs(self):
        print(f"{self.name} lays eggs")

class Dog(Mammal):
    def speak(self):
        print(f"{self.name} barks")

class Cat(Mammal):
    def speak(self):
        print(f"{self.name} meows")

class Parrot(Bird):
    def speak(self):
        print(f"{self.name} talks")

# Creating instances and demonstrating hierarchical inheritance
dog = Dog("Buddy")
cat = Cat("Whiskers")
parrot = Parrot("Polly")

print("Dog:")
dog.speak()
dog.give_birth()


print("\nCat:")
cat.speak()
cat.give_birth()

print("\nParrot:")
parrot.speak()
parrot.lay_eggs()
