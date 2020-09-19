class Pets():
    animals = []
    def __init__(self,animals):
        self.animals=animals
    
    def walk(self):
        for animal in self.animals:
            print(animal.walk())
class Cat():
    is_lazy = True
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def walk(self):
        return f'{self.name} is just walking around'
class Simon(Cat):
    def sing(self,sounds):
        return f'{sounds}'

class Sally(Cat):
    def sing(self,sounds):
        return f'{sounds}'

class Tom(Cat):
    def sing(self,sounds):
        return f'{sounds}'

cat_one = Simon('kate',5)
cat_two = Sally('Luna',4)
cat_three = Tom('Jade',1)
my_cats = [Simon('Simon',15), Sally('Sally',12), Tom('Tom',11)]

my_pets = Pets(my_cats)
my_pets.walk()

'''cat_one = Cat('kate',5)
cat_two = Cat('Luna',4)
cat_three = Cat('Jade',1)

def oldest_cat(*args):
    ages = []
    for x in args:
        ages.append(x.age)
    return max(ages)

if __name__=='__main__':
    print(f'The oldest cat is {oldest_cat(cat_one,cat_three,cat_three)} years old')
'''
