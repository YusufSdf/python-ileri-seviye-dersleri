# with open("csv-ornek.csv") as file:
#     print(file.read())
import re
import csv

with open("usarname.csv") as file:
    csv_ = csv.reader(file)
    # liste = list(csv_)
    next(csv_)
    for i in csv_: # zaten oto listeye dönüştürüyor
        if i[4] == "True":
            print(i[3])
        else:
            print(i[1])

