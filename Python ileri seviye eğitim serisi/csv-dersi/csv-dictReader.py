import csv

with open("usarname.csv") as file:
    csv_ = csv.DictReader(file,delimiter=",") # deliminter default olarak virgül,,, amacı ayrım yapan şey
    for i in csv_:
        # print(i["Username"])
        # print(i.get("Username"))
        # if i.get("Check") == "True":
        #     print(i["Username"])
        result = i.get("Username").isalpha()
        if  result:
            print(i.get("First name"))


    