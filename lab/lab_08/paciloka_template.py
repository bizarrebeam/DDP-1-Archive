class Hotel:
    def __init__(self, name, available_room, room_price):
        self.name = name
        self.available_room = available_room
        self.room_price = room_price
        self.guest = set()  
        self.profit = 0

    def booking(self, user, jumlah_kamar):
        if jumlah_kamar < 0:
            print("Jumlah kamar yang akan dipesan harus lebih dari 0!")
        if jumlah_kamar > 0 and self.available_room >= jumlah_kamar and user.money >= jumlah_kamar * self.room_price:
            self.profit += jumlah_kamar * self.room_price
            user.money -= jumlah_kamar * self.room_price
            self.available_room -= jumlah_kamar
            self.guest.add(user.name)  
            user.hotel_list.add(self.name)  
            return True
        else:
            return False

    def __str__(self):
        return f"{self.name} | {', '.join(self.guest)}"

class User:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.hotel_list = set()  

    def topup(self, jumlah_topup):
        if jumlah_topup > 0:
            self.money += jumlah_topup
            return True
        else:
            return False  
        
    def __str__(self):
        return f"{self.name} | {', '.join(self.hotel_list)}"

if __name__ == '__main__':
    hotels = []
    users = []

    banyak_hotel = int(input('Masukkan banyak hotel: '))
    banyak_user = int(input('Masukkan banyak user: '))
    print()

    for i in range(banyak_hotel):

        nama_hotel = input(f"Masukkan nama hotel ke-{i + 1}: ")
        banyak_kamar_hotel = int(input(f"Masukkan banyak kamar hotel ke-{i + 1}: "))  
        harga_kamar = int(input(f"Masukkan harga satu kamar hotel ke-{i + 1}: ")) 
        hotels.append(Hotel(nama_hotel, banyak_kamar_hotel, harga_kamar))
    print()    
    for j in range(banyak_user):

        nama_user = input(f"Masukkan nama user ke-{j + 1}: ")
        saldo_user = int(input(f"Masukkan saldo user ke-{j + 1}: "))  
        users.append(User(nama_user, saldo_user))
    
    while True:
        print()
        print("=============Welcome to Paciloka!=============")
        print()
        perintah = int(input("Masukkan perintah: "))

        if perintah == 1:
            print("Daftar Hotel")
            for i, hotel in enumerate(hotels, 1):
                print(f"{i}. {hotel.name}")
            print()
            print("Daftar user")
            for j, user in enumerate(users, 1):
                print(f"{j}. {user.name}")
        elif perintah == 2:
            hotel_name = input("Masukkan nama hotel: ")
            found_hotel = None
            for hotel in hotels:
                if hotel.name == hotel_name:
                    found_hotel = hotel
                    break
            if found_hotel:
                print(f"Hotel dengan nama {hotel_name} mempunyai profit sebesar {found_hotel.profit}")
            else:
                print(f"Nama hotel tidak ditemukan di sistem!")

        elif perintah == 3:
            user_name = input('Masukkan nama user: ')
            found_user = None
            for user in users:
                if user.name == user_name:
                    found_user = user
                    break
            if found_user:
                print(f"User dengan nama {user_name} mempunyai saldo sebesar {found_user.money}")
            else:
                print(f"Nama user tidak ditemukan di sistem!")
        
        elif perintah == 4:
            user_name = input("Masukkan nama user: ")
            found_user = None
            for user in users:
                if user.name == user_name:
                    found_user = user
                    break
            if found_user:
                jumlah_uang = int(input("Masukkan jumlah uang yang akan ditambahkan ke user: "))
                if found_user.topup(jumlah_uang):
                    print(f"Berhasil menambahkan {jumlah_uang} ke user {user_name}. Saldo user menjadi {found_user.money}")
                else:
                    print("Jumlah saldo yang akan ditambahkan ke user harus lebih dari 0!")
            else:
                print(f"Nama user tidak ditemukan di sistem!")
        
        elif perintah == 5:
            user_name = input("Masukkan nama user : ")
            found_user = None
            for user in users:
                if user.name == user_name:
                    found_user = user
                    break
            if found_user is None:
                print("Nama user tidak ditemukan di sistem!")
                continue
            
            hotel_name = input("Masukkan nama hotel : ")        
            found_hotel = None
            for hotel in hotels:
                if hotel.name == hotel_name:
                    found_hotel = hotel
                    break
            if found_hotel is None:
                print("Nama hotel tidak ditemukan di sistem!")
                continue

            if found_user and found_hotel:
                jumlah_kamar = int(input("Masukkan jumlah kamar yang akan dibooking : "))
                if found_hotel.booking(found_user, jumlah_kamar):
                    print(f"User dengan nama {user_name} berhasil melakukan booking di hotel {hotel_name} dengan jumlah {jumlah_kamar} kamar!")
                else:
                    print("Booking tidak berhasil!")


        elif perintah == 6:
            hotel_name = input("Masukkan nama hotel: ")
            found_hotel = None
            for hotel in hotels:
                if hotel.name == hotel_name:
                    found_hotel = hotel
                    break
            if found_hotel:
                if found_hotel.guest:
                    print(found_hotel)
                else:
                    print(f"Hotel {hotel_name} tidak memiliki pelanggan!")
            else:
                print(f"Nama hotel tidak ditemukan di sistem!")

        elif perintah == 7:
            user_name = input("Masukkan nama user: ")
            found_user = None
            for user in users:
                if user.name == user_name:
                    found_user = user
                    break
            if found_user:
                if found_user.hotel_list:
                    print(found_user)
                else:
                    print(f"User {user_name} tidak pernah melakukan booking!")
            else:
                print(f"Nama user tidak ditemukan di sistem!")

        elif perintah == 8:
            print("Terima kasih sudah mengunjungi Paciloka!")
            break

        else:
            print("Perintah tidak diketahui! Masukkan perintah yang valid")

