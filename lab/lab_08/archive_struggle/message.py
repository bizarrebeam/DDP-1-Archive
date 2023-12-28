class Hotel:
    def __init__(self, name, available_room, room_price):
        self.name = name
        self.available_room = available_room
        self.room_price = room_price
        self.profit = 0
        self.guest = []

    def booking(self, user, num_rooms):
        if num_rooms <= 0:
            print("Jumlah kamar yang akan dipesan harus lebih dari 0!")
            return False

        if num_rooms > self.available_room:
            print("Booking tidak berhasil! Jumlah kamar yang tersedia tidak mencukupi.")
            return False

        total_price = num_rooms * self.room_price
        if user.money < total_price:
            print("Booking tidak berhasil! Saldo tidak mencukupi.")
            return False

        self.profit += total_price
        self.available_room -= num_rooms

        if user.name not in self.guest:
            self.guest.append(user.name)

        user.money -= total_price
        if self.name not in user.hotel_list:
            user.hotel_list.append(self.name)

        return True

    def __str__(self):
        return f"{self.name} | {', '.join(self.guest)}"



class User:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.hotel_list = []

    def topup(self, amount):
        if amount <= 0:
            print("Jumlah saldo yang akan ditambahkan ke user harus lebih dari 0!")
            return

        self.money += amount
        print(f"Berhasil menambahkan {amount} ke user {self.name}. Saldo user menjadi {self.money}")

    def __str__(self):
        return f"{self.name} | {', '.join(self.hotel_list)}"


def main():
    print("=============Welcome to Paciloka!=============")
    
    num_hotels = int(input("Masukkan banyak hotel : "))
    num_users = int(input("Masukkan banyak user : "))

    hotels = []
    users = []

    for i in range(num_hotels):
        name = input(f"\nMasukkan nama hotel ke-{i+1} : ")
        available_room = int(input(f"Masukkan banyak kamar hotel ke-{i+1} : "))
        room_price = int(input(f"Masukkan harga satu kamar hotel ke-{i+1} : "))
        hotels.append(Hotel(name, available_room, room_price))

    for i in range(num_users):
        name = input(f"\nMasukkan nama user ke-{i+1} : ")
        money = int(input(f"Masukkan saldo user ke-{i+1} : "))
        users.append(User(name, money))

    while True:
        print("\n=============Welcome to Paciloka!=============")
       
        command = input("Masukkan perintah : ")

        if command == "1":
            print("\nDaftar Hotel")
            for i, h in enumerate(hotels, 1):
                print(f"{i}. {h.name}")
            
            print("\nDaftar User")
            for i, u in enumerate(users, 1):
                print(f"{i}. {u.name}")

        elif command == "2":
            hotel_name = input("Masukkan nama hotel : ")
            found = False
            for h in hotels:
                if h.name == hotel_name:
                    print(f"Hotel dengan nama {hotel_name} mempunyai profit sebesar {h.profit}")
                    found = True
                    break
            if not found:
                print(f"Hotel dengan nama {hotel_name} tidak ditemukan!")

        elif command == "3":
            user_name = input("Masukkan nama user : ")
            found = False
            for u in users:
                if u.name == user_name:
                    print(f"User dengan nama {user_name} mempunyai saldo sebesar {u.money}")
                    found = True
                    break
            if not found:
                print(f"Nama user tidak ditemukan di sistem!")

        elif command == "4":
            user_name = input("Masukkan nama user : ")
            found = False
            for u in users:
                if u.name == user_name:
                    amount = int(input("Masukkan jumlah uang yang akan ditambahkan ke user : "))
                    if amount > 0:
                        u.topup(amount)
                    else:
                        print("Jumlah saldo yang akan ditambahkan ke user harus lebih dari 0!")
                    found = True
                    break
            if not found:
                print(f"Nama user tidak ditemukan di sistem!")

        elif command == "5":
            user_name = input("Masukkan nama user: ")
            found_user = None

            for u in users:
                if u.name == user_name:
                    found_user = u
                    break

            if found_user:
                hotel_name = input("Masukkan nama hotel: ")
                found_hotel = None

                for h in hotels:
                    if h.name == hotel_name:
                        found_hotel = h
                        break

                if found_hotel:
                    try:
                        num_rooms = int(input("Masukkan jumlah kamar yang akan dibooking: "))
                        if num_rooms <= 0:
                            print("Jumlah kamar yang akan dipesan harus lebih dari 0!")
                        elif num_rooms > found_hotel.available_room:
                            print("Booking tidak berhasil!")
                        elif found_user.money < num_rooms * found_hotel.room_price:
                            print("Booking tidak berhasil! Saldo tidak mencukupi.")
                        else:
                            found_hotel.booking(found_user, num_rooms)
                            print(f"User dengan nama {found_user.name} berhasil melakukan booking di hotel {found_hotel.name} dengan jumlah {num_rooms} kamar!")
                    except ValueError:
                        print("Masukkan jumlah kamar yang valid (angka).")

                else:
                    print(f"Nama hotel tidak ditemukan di sistem!")

            else:
                print(f"Nama user tidak ditemukan di sistem!")



        elif command == "6":
            hotel_name = input("Masukkan nama hotel : ")
            found = False
            for h in hotels:
                if h.name == hotel_name:
                    if not h.guest:
                        print(f"Hotel {hotel_name} tidak memiliki pelanggan!")
                    else:
                        print(str(h))
                    found = True
                    break
            if not found:
                print(f"Nama hotel tidak ditemukan!")

        elif command == "7":
            user_name = input("Masukkan nama user : ")
            found = False
            for u in users:
                if u.name == user_name:
                    if not u.hotel_list:
                        print(f"User {user_name} tidak pernah melakukan booking!")
                    else:
                        print(str(u))
                    found = True
                    break
            if not found:
                print(f"User {user_name} tidak ditemukan!")

        elif command == "8":
            print("Terima kasih sudah mengunjungi Paciloka!")
            break

        else:
            print("Perintah tidak diketahui! Masukkan perintah yang valid")


if __name__ == "__main__":
    main()
