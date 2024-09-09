import json

data = {
        "2": {
        "title":"Macbook Pro",
        "price": 90000,
        "rating": "4.5",
        "category": "Bilgisayar",
        "colors": ["Red","Blue"]},

        "3":{
        "title":"Macbook air",
        "price": 80000,
        "rating": "4.5",
        "category": "Bilgisayar",
        "colors": ["black","Blue"]}
}

product = {
        "1": { 
        "title":"samsung s24",
        "price": 60000,
        "rating": "4.5",
        "category": "telefon",
        "colors": ["black"]}
}

with open("products.json") as file:
    products = json.load(file)
print(products["2"])

products.update({"4": { 
        "title":"iphone 14",
        "price": 40000,
        "rating": "4.5",
        "category": "telefon",
        "colors": ["purple"]}})

products.pop("2")

with open("products.json","w",encoding="utf-8") as file:
    json.dump(products, file, ensure_ascii=False,indent=2)