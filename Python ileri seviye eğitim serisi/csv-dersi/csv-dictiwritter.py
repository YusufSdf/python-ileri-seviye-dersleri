import csv

# with open("yeni.csv","w",newline="") as file:
#     headers = ["Username", "Identifier","First name","Last name","Check"]
#     csv_writter = csv.DictWriter(file, headers)
#     csv_writter.writeheader()
#     csv_writter.writerow({
#         "Username": "ysf1",
#         "Identifier": 10,
#         "First name":"yusuf",
#         "Last name":"sedef",
#         "Check":"True"
#     })

with open("username.csv") as f:
    csv_ = csv.DictReader(f)
    urunler = list(csv_)
    with open("yeni.csv","a",newline="") as file:
            headers = ["Username", "Identifier","First name","Last name","Check"]
            csv_writter = csv.DictWriter(file, headers)
            csv_writter.writeheader()
            csv_writter.writerow({
                "Username": "ysf1",
                "Identifier": 10,
                "First name":"yusuf",
                "Last name":"sedef",
                "Check":"True"
            })