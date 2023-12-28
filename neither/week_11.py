class Cat:

    def __init__(self, name, age, breed, color):

        self.name = name

        self.age = age

        self.breed = breed

        self.color = color

 

    def cat_description(self):

        print("Kucing bernama {} adalah kucing {} dengan warna {} dengan umur {} tahun.".format(self.name,self.breed, self.color, self.age) )

meong = Cat("budi", "100", "kampung", "item")
print(meong.cat_description())
