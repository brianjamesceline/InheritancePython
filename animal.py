class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return f"My name is {self.name}"

# class dog inherits from animal
class Dog(Animal):
    def __init__(self, name, age):
        # self.name = name
        # self.age = age
        # alternatively you can use a super method
        super().__init__(name, age)

    # when using speak, it will now refer to class Dog and NOT class animal
    def speak(self):
        return "whoof whoof!"

# class dog inherits from animal
class Cat(Animal):
    def __init__(self, name, age):
        # self.name = name
        # self.age = age
        # alternatively you can use
        super().__init__(name, age)
