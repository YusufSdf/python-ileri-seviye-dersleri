import json

# with open("product.json") as file:
#     data = json.load(file) # eğer başka yerden veri çekeceksek bu
#     print(data["title"])


data =  """
    {
        "id":1,
        "title":"Macbook Pro",
        "price": 90000,
        "rating": "4.5",
        "category": "Bilgisayar",
        "colors": ["Red","Blue"]
}
"""
data = json.loads(data) # eğer uygulama içinden veri çekeceksek bu
print(data["title"])

