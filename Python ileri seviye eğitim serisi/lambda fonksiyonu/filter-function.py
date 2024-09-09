numbers = [1,2,3,-4,-5,6]

result = list(filter(lambda x: x < 0, numbers))
print(result)

students = [
    {"name":"yusuf","note":100},
    {"name":"asel","note":90},
    {"name":"ilsu","note":70},
]

resultfilt = list(filter(lambda x: x["note"] > 75, students))
result = list(map(lambda y: y["name"],resultfilt))


print(result)
