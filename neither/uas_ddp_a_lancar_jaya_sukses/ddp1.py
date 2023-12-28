with open ('ddp1.txt', 'rb') as x:
    x.seek(5) # got to the 5th byte
    print(x.read(4).decode('utf-8')) # start to read sebanyak 4 byte, output: asik
    x.seek(11) # sampai di ujung /n 
    print(x.read(4).decode('utf-8')) # baca 4 byte, ddp2
    print(x.tell())