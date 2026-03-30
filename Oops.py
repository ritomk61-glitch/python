class Animal:
    def __init__(self, name):
        self.name = name
        self._type = "Animal"

    def speak(self):
        return "This animal makes a sound"

    def info(self):
        return f"Name: {self.name}, Type: {self._type}"


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


dog = Dog("Tommy", "German Shepherd")
cat = Cat("Kitty")

print(dog.info())
print("Dog says:", dog.speak())
print()
print(cat.info())
print("Cat says:", cat.speak())