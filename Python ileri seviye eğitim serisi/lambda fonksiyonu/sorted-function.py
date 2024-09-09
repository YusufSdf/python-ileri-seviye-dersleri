
katilim = [
    {"name":"python","count":1000},
    {"name":"java","count":600},
    {"name":"html","count":500},
]

result = sorted(katilim, key= lambda x: x["count"])
result2= list(map(lambda y: y["name"],result))
print(result2)