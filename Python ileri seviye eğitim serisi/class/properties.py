class Product:
    def __init__(self, name="yusuf"):
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self.new_name = new_name
        if len(self.new_name) > 5:
            print("hata")
        else:
            self._name = new_name
            print(self._name)


p1 = Product()
p1.name = "yusufyusuf"
p1.name = "ilsu"

# print(p1.name)