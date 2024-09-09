
class Cartıtem:
    def __init__(self, name,price):
        self.name = name
        self.price = price

item1 = Cartıtem("samsung s24", 2000)
item2 = Cartıtem("samsung s25", 3000)
item3 = Cartıtem("samsung s26", 4000)

class shoppingCard:
    def __init__(self, liste):
        self.liste = liste
    def adding(self, item):
        self.liste.append(item)
    def display(self):
        for i in self.liste:
            print(i[0],i[1])
    def total(self):
        return sum([item.price for item in self.liste])



sc = shoppingCard([item1,item2])
sc.adding(item3)
sc.display()
sc.total()





