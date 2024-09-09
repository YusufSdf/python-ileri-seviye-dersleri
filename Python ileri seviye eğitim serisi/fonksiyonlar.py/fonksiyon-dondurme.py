# def taban(number):
#     def us(number2):
#         return number ** number2
#     return us
# result = taban(2)(3)
# print(result)


# def yetki(role):
#     def site_(site):
#         if role == "admin":
#             print(f"{site} başarılı")
#         else:
#             print(f"{site} başarısız")
#     return site_

# result = yetki("admin")


def islemAdi(islem):
    def toplam(*args):
        top = 0
        for i in args:
            top +=i
        return top
    def carpim(*args):
        crp = 1
        for i in args:
            crp *= i
        return crp
    
    if islem == "toplam":
        return toplam
    else:
        return carpim

toplama = islemAdi("toplam")
carpma = islemAdi("carpim")

result = toplama(10,20,30)
# result = carpma(10,20,30)

print(result)
