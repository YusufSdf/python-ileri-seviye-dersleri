
result = all([True,True,False]) # hepsi true mu
result = any([True,True,False]) # herhangi biri true mu


users = ["yusuf","ali","asel","ilsu"]

result = all(use[0] == "a" for use in users) # hepsi a harfi ile mi başlıyor
result = any(len(use) == 4 for use in users) # herhangi bir kelime 4 harfli mi 


print(result)