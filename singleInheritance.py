# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} says something.")

# Child class inheriting from Animal
class Dog(Animal):
    def bark(self):
        print(f"{self.name} barks: Woof!")

# Creating an instance of the child class
my_dog = Dog("Buddy")

# Accessing the attributes and methods from both parent and child classes
print(f"Name: {my_dog.name}")
my_dog.speak()
my_dog.bark()
