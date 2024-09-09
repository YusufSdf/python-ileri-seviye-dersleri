liste = [number for number in range(101) if number % 12 == 0]

text = "hello 12345 world"

liste =[num for num in text if num.isnumeric() == True]

temp = [10,20,-5,-3,6,-7]

liste = [i if i > 0  else "buzlanma tehlikesi" for i in temp]

students = ["ali","yusuf","ilsu"]
nots = [50,60,80]


liste = {(students[i], nots[i]) for i in range(0,len(students))}
liste_dict = {key:value for key,value in liste if value > 50}

result = [(x,y) for x in range(3) for y in range(3)]


print(result)
