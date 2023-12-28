with open("fasilkom.txt", "r" ) as x :
    x.seek(5)
    x.read(5)
    print(x.tell())
    x.seek(15)
    print(x.read(2))