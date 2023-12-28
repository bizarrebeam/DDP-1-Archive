class Hotel :
    def __init__(self, name, available_room, room_price):
        self.name = name
        self.available_room = available_room
        self.room_price = room_price
        self.profit = 0
        self.guest = []

    
    def booking(self, user, rooms_num):
        if self.available_room >= rooms_num > 0:
            price = rooms_num * self.room_price

            if user.money >= price:
                user.money -= price

                self.profit += price
                self.available_room -= rooms_num
                
                if user.name not in self.guest:
                    self.guest.append(user.name)

                if self.name not in user.hotel_list:
                    user.hotel_list.append(self.name)

                print("User dengan nama {} berhasil melalukan booking di hotel {}"\
                    "dengan jumlah {} kamar!".format(user.name, self.name, rooms_num))
            else:
                print("{} tidak memiliki saldo cukup untuk melakukan booking!".format(user.name))
        else:
            print("Jumlah kamar yang akan dipesan harus leboh dari 0!")  
    
    def get__guest(self):
        return self.guest

    def __str__(self):
        return f"{self.name} | {', '.join(self.guest)}"

class User:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.hotel_list = []
                
    def topup(self, amount):
        if amount > 0:
            self.money += amount
            print("Berhasil menambahkan {} ke user {}. Saldo user menjadi"\
                .format(amount, self.name, self.money))

        else:
            print("Jumlah saldo yang akan ditambahkan ke user harus lebih dari 0!")
    
    def get_booked_hotels(self):
        return self.hotel_list

    def __str__(self):
        return f"{self.name} | {', '.join(self.hotel_list)}"

def find_hotel(hotels, name):
    for hotel in hotels:
        if hotel.name == name:
            return hotel
    return None

def find_user(users, name):
    for user in users:
        if user.name == name:
            return user
    return None

def main():
    hotels_num = int(input("Masukkan banyak hotel: "))
    users_num = int(input("Masukkan banyak user: "))

    hotels = []
    users = []

    for i in range(1, hotels_num + 1):
        name = input("Masukkan nama hotel ke-{}: ".format(i))
        rooms = int(input("Masukkan banyak kamar hotel ke-{}: ".format(i)))
        price = int(input("Masukkan harga satu kamar hotel ke-{}: ".format(i)))
        
        hotel = Hotel(name, rooms, price)
        hotels.append(hotel)
        
    for j in range(1, users_num + 1):
        name = input("Masukkan nama user ke-{}: ".format(j))
        balance = int(input("Masukkan saldo user ke-{}: ".format(j)))

        user = User(name, balance)
        users.append(user)
        
    while True:
        print("\n=============Welcome to Paciloka!=============")
        action = input("Masukkan aksi:")

        if action == "1":
            print("\nDaftar Hotel:")
            for hotel in hotels:
                print(f"{hotel.name}")

            print("\nDaftar User:")
            for user in users:
                print(f"{user.name}")
        
        elif action == "2":
            hotel_name = input("Masukkan nama hotel: ")
            found_hotel = find_hotel(hotels, hotel_name)
            
            if found_hotel:
                print("Hotel dengan nama {} mempunyai tamu {}".format(hotel_name, found_hotel.get_the_guest()))
            else:
                print("Hotel dengan nama {} tidak ditemukan!".format(hotel_name))

        elif action == "3":
            user_name = input("Masukkan nama user: ")
            found_user = find_user(users, user_name)
            if found_user:
                print("User dengan nama {} mempunyai saldo sebesar {}".format(user_name, found_user.money))
            else:
                print("User dengan nama {} tidak ditemukan!".format(user_name))

        elif action == "4":
            user_name = input("Masukkan nama user: ")
            found_user = find_user(users, user_name)

            if found_user:
                amount = int(input("Masukkan jumlah uang yang akan ditambahkan ke user: "))
                if amount > 0:
                    found_user.topup(amount)
                else:
                    print("Jumlah saldo yang akan ditambahkan ke user harus lebih dari 0!")
            else:
                print("Error: User dengan nama {} tidak ditemukan!".format(user_name))

        elif action == "5":
            user_name = input("Masukkan nama user: ")
            hotel_name = input("Masukkan nama hotel: ")
            found_user = find_user(users, user_name)
            found_hotel = find_hotel(hotels, hotel_name)

            if found_user and found_hotel:
                num_rooms = int(input("Masukkan jumlah kamar yang akan dibooking: "))
                found_hotel.booking(found_user, num_rooms)
            else:
                print("Error: Nama user atau nama hotel tidak ditemukan!".format(user_name, hotel_name))

        elif action == "6":
            hotel_name = input("Masukkan nama hotel: ")
            found_hotel = find_hotel(hotels, hotel_name)

            if found_hotel:
                guests = found_hotel.get_guests()
                if guests:
                    print("{}\n".format(found_hotel))
                else:
                    print("Hotel {} tidak memiliki pelanggan!".format(hotel_name))
            else:
                print("Error: Hotel dengan nama {} tidak ditemukan!".format(hotel_name))

        elif action == "7":
            user_name = input("Masukkan nama user: ")
            found_user = find_user(users, user_name)

            if found_user:
                booked_hotels = found_user.get_booked_hotels()
                if booked_hotels:
                    print("{}\n".format(found_user))
                else:
                    print("{} tidak pernah melakukan booking!".format(user_name))
            else:
                print("Error: User dengan nama {} tidak ditemukan!".format(user_name))

        elif action == "8":
            print("Terima kasih sudah mengunjungi Paciloka!")
            break

        else:
            print("Perintah tidak diketahui! Masukkan perintah yang valid")



if __name__ == "__main__":
    main()




if __name__ == '__main__':
    main()