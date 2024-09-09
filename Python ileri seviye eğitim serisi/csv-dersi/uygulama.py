import csv

# with open("onlinefoods.csv") as file:
#     csv_reader = csv.DictReader(file)
#     liste = list(csv_reader)
#     print(len(liste)- 1)
#     # a = 0
#     # for i in csv_reader:
#     #     a +=1
#     # print(a)

# with open("onlinefoods.csv") as file:
#     csv_reader = csv.DictReader(file)
#     print(len([i.get("Age") for i in csv_reader if i.get("Occupation")== "Student"]))

with open("onlinefoods.csv") as file:
    csv_reader = csv.DictReader(file)
    print([i.get("Pin code") for i in csv_reader if 20 < int(i.get("Age")) < 30])