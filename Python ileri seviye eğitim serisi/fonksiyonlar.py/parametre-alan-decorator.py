def count(count): 
    def selamlama(fn):
        def inner(name):
            print(f"selam {name}")
            for i in range(count):
                fn(name)
            print("görüşürüz")
        return inner
    return selamlama

# fonksiyon çağırılmadan önce decorator okunur, selamlama içindeki fn kısmına önündeki fonksiyonu gönderir
@count(2)
def günaydın(name):
    print(f"günaydın {name}")

@count(3)
def iyigunler(name):
    print(f"iyi günler {name}")

# result = selamlama(günaydın)
# result

iyigunler("yusuf")



