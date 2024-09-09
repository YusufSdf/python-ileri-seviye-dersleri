import json

data = {
        "id":1,
        "title":"Macbook Pro",
        "price": 90000,
        "rating": "4.5",
        "category": "Bilgisayar",
        "colors": ["Red","Blue"]
}


with open("urunler.json","w",encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False,indent=2)
