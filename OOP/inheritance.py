class User():
    def __init__(self,name):
        self.name=name
    def sign_in(self):
        print(f'{self.name} is logged in')
    
class Wizard(User):
    def __init__(self,name,power):
        super(Wizard,self).__init__(name)
        self.power = power

    def attack(self):
        print(f'{self.name} Attacking with power of {self.power}')

class Archer(User):
    def __init__(self,name,arrows):
        super().__init__(name)
        self.arrows=arrows
    
    def attack(self):
        print(f'{self.name} Attacking with number of arrows left {self.arrows}')
wiz = Wizard('Gandalf',10000)
arch = Archer('Legolas',200)
players =[wiz,arch]
for player in players:
    player.sign_in()
    player.attack()
