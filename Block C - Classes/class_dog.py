class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")

    def get_info(self):
        print(f"{self.name} is {self.age} years old.")

dog1 = Dog("Rex", 5)
dog1.bark()
dog1.get_info()

dog2 = Dog("Buddy", 3)
dog2.bark()
dog2.get_info()