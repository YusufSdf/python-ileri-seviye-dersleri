def selamlama(fn):
    def inner(name):
        print(f"selam {name}")
        fn(name)
        print("görüşürüz")
    return inner

# fonksiyon çağırılmadan önce decorator okunur, selamlama içindeki fn kısmına önündeki fonksiyonu gönderir
@selamlama 
def günaydın(name):
    print(f"günaydın {name}")

@selamlama
def iyigunler(name):
    print(f"iyi günler {name}")

# result = selamlama(günaydın)
# result

iyigunler("yusuf")



