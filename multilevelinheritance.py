class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} barks")

class Labrador(Dog):
    def swim(self):
        print(f"{self.name} can swim")

# Creating instances of each class
animal_instance = Animal("Generic Animal")
dog_instance = Dog("Buddy")
labrador_instance = Labrador("Max")

# Calling methods
print("Calling methods of Animal class:")
animal_instance.speak()

print("\nCalling methods of Dog class:")
dog_instance.speak()
dog_instance.bark()

print("\nCalling methods of Labrador class:")
labrador_instance.speak()
labrador_instance.bark()
labrador_instance.swim()
