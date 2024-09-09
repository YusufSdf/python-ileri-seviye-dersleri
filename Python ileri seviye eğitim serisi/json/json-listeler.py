
# data = [
# {
#         "id":1,
#         "title":"Macbook Pro",
#         "price": 90000,
#         "rating": "4.5",
#         "category": "Bilgisayar",
#         "colors": ["Red","Blue"]
# },
# {
#         "id":2,
#         "title":"Macbook air",
#         "price": 80000,
#         "rating": "4.5",
#         "category": "Bilgisayar",
#         "colors": ["black","Blue"]
# }
# ]
# import json

# product = {
#         "id":3,
#         "title":"samsung s24",
#         "price": 60000,
#         "rating": "4.5",
#         "category": "telefon",
#         "colors": ["black"]
# }

# with open("products.json") as file:
#     products = json.load(file)

# for i in products:
#     print(i["title"])
#     if i["title"] == "samsung s24":
#         i["title"] == "samsung a55"

# # products.append(product)

# with open("products.json","w",encoding="utf-8") as file:
#     json.dump(products, file, ensure_ascii=False,indent=2)