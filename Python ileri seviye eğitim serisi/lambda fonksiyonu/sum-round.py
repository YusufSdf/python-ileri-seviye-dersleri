numbers = [1,2,3,4,5,6,7,8,9]

katilim = [
    {"name":"python","count":1000},
    {"name":"java","count":600},
    {"name":"html","count":500},
]

result = sum(prc["count"] for prc in katilim)

result = round(2.4) # yuvarlar
result = round(2.46745,3) 


print(result)