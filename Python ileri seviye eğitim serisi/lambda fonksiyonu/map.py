
numbers = [1,2,3,4,5,6]

result = list(map(lambda num: num **2 , numbers)) 

my_dict = [
    {"name":"yusuf", "soyad":"sedef"},
    {"name":"ilsu", "soyad":"sedef"}
]

result = list(map(lambda kisi: kisi["name"], my_dict))

print(result)