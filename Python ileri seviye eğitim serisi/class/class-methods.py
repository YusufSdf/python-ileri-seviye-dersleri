class Cartıtem:
    def __init__(self, name,price,number):
        discount_ = 0.8
        self.name = name
        self.price = price
        self.number = number
    def discount(self):
        self.price = Cartıtem.discount_ * self.price # fiyatı indirim ile günceller
    def prc(self):
        return  self.price * self.number 
        


item1 = Cartıtem("samsung s24",45000,4) 
item2 = Cartıtem("samsung s34",65000,5) 
item3 = Cartıtem("samsung s44",75000,8) 

print(item1.prc())
print(item2.prc())
print(item3.prc())



