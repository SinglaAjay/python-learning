# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound"


# Child class inheriting from Animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks"


# Example usage
dog = Dog("Buddy")
print(dog.speak())  # Output: Buddy barks..

animal=Animal("Generic Animal")
print(animal.speak())  # Output: Generic Animal makes a sound