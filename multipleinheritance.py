# Parent class 1
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

# Parent class 2
class Flyable:
    def fly(self):
        print(f"{self.name} can fly.")

# Parent class 3
class Swimmable:
    def swim(self):
        print(f"{self.name} can swim.")

# Child class inheriting from Animal, Flyable, and Swimmable
class Bird(Animal, Flyable, Swimmable):
    def speak(self):
        print(f"{self.name} says Chirp!")

# Child class inheriting from Animal and Swimmable
class Fish(Animal, Swimmable):
    def speak(self):
        print(f"{self.name} says Blub!")

# Create instances of the classes
bird_instance = Bird("Sparrow")
fish_instance = Fish("Goldfish")

# Demonstrate method calls
bird_instance.speak()
bird_instance.fly()
bird_instance.swim()

fish_instance.speak()
fish_instance.swim()
