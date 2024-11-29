#Зачем нужно наследование: Съедобное, несъедобное.
class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False
    def eat(self, food):

        if food.edible: # обращаемся к атрибуту объекта Plant
            print(f"{self.name},  съел , {food.name}")
            self.fed = True# обращаемся к атрибуту объекта класса Animal
        else:
            print(f"{self.name}, не съел , {food.name}")
            self.alive = False # обращаемся к атрибуту объекта класса Animal

class Mammal(Animal):
    pass

class Predator(Animal):
    pass

class Plant:
    def __init__(self, name ):
        self.edible = False
        self.name = name
class Flower(Plant):
    pass

class Fruit(Plant):
    def __init__(self,name):
        super().__init__(name)
        self.edible = True


a1 = Predator('Волк с Уолл-Стрит')

a2 = Mammal('Хатико')

p1 = Flower('Цветик семицветик')

p2 = Fruit('Заводной апельсин')

print(a1.name)

print(p1.name)

print(a1.alive)

print(a2.fed)

a1.eat(p1)

a2.eat(p2)

print(a1.alive)

print(a2.fed)