class Mammal:
    def __init__(self, name):
        self.name = name  # can be any type no type checking

    def run(self):
        print(f"{self.name} runs")

    def eat(self):
        print(f"{self.name} eats")

    def jump(self):
        print(f"{self.name} jumps")


class Dog(Mammal):
    def bark(self):
        print(f"{self.name} barks")


class Cat(Mammal):
    def meow(self):
        print(f"{self.name} meows")


dogJoe = Dog("Joe")
catRee = Cat("Ree")
dogJoe.food = "pedegree"
catRee.food = "whiskas"
dogJoe.age = 2
catRee.age = 3
dogJoe.bark()
catRee.meow()

catRee.run()
dogJoe.jump()
print(catRee.food)
print(catRee.age)
print(dogJoe.food)
print(dogJoe.age)
