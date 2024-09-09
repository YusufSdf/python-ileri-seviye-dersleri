import json


class Product:
    def __init__(self,id,title,price):
        self.id = id
        self.title = title
        self.price = price
# # serializing
# p1 = Product(1,"samsung s24",70000)
# p2 = Product(1,"samsung s25",80000)

# products = [p1.__dict__,p2.__dict__]

# with open("new_products.json","w") as file:
#     json.dump(products, file)

#deserializing 

with open("new_products.json") as file:
    products = json.load(file)

urunler =  []
for key,value in products.items():
    urunler.append(Product(key,value["title"],value["price"]))


