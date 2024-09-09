names = ["ali","yusuf","ilsu","asel"]

result = min(names)
result = max(names, key= lambda y: y)

products = [
    {"name":"samsung s23", "price":100},
    {"name":"samsung s24", "price":300},
    {"name":"samsung s24", "price":400},
]

result = min(products, key= lambda prc: prc["price"])

print(result["name"])


