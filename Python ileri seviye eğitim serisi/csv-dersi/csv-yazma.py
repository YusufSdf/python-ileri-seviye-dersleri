import csv

with open("arabalar.csv","w",newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["marka","model"])
    csv_writer.writerow(["toyota","corolla"])
    # csv_writer.writerow(["renault","clio"])
    # csv_writer.writerows([["marka","model"],["toyota","corolla"]])

with open("arabalar.csv","a",newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["renault","clio"])