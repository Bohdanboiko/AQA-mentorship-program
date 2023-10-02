class Creature:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name})"

    def say(self):
        return "Я тварина"

    def act(self):
        return "Я живу"


class Animal(Creature):
    def say(self):
        return "Я - тварина"

    def act(self):
        return "Я живу"


class Bird(Creature):
    def say(self):
        return "Я - птах"

    def act(self):
        return "Я літаю"


class Dog(Animal):
    def say(self):
        return "Гав"

    def act(self):
        return "Я охороняю"


class Duck(Bird):
    def say(self):
        return "Кря"

    def act(self):
        return "Я плаваю"



farm_dog = Dog("Ніка")
farm_duck = Duck("Качка")

print(farm_dog)
print(farm_dog.say())
print(farm_dog.act())

print(farm_duck)
print(farm_duck.say())
print(farm_duck.act())
