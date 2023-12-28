
class Hotel:
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

                print(f"User dengan nama {user.name} berhasil melakukan booking di hotel {self.name} dengan jumlah {rooms_num} kamar!")
            else:
                print(f"{user.name} tidak memiliki saldo cukup untuk melakukan booking!")
        else:
            print("Jumlah kamar yang akan dipesan harus lebih dari 0!")

    def get_guests(self):
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
            print(f"Berhasil menambahkan {amount} ke user {self.name}. Saldo user menjadi {self.money}")
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
        name = input(f"Masukkan nama hotel ke-{i}: ")
        rooms = int(input(f"Masukkan banyak kamar hotel ke-{i}: "))
        price = int(input(f"Masukkan harga satu kamar hotel ke-{i}: "))

        hotel = Hotel(name, rooms, price)
        hotels.append(hotel)

    for j in range(1, users_num + 1):
        name = input(f"Masukkan nama user ke-{j}: ")
        balance = int(input(f"Masukkan saldo user ke-{j}: "))

        user = User(name, balance)
        users.append(user)

    while True:
        print("\n=============Welcome to Paciloka!=============")
        print("Masukkan perintah:")
        print("1. Cetak semua nama hotel dan user")
        print("2. Cetak profit dari sebuah hotel")
        print("3. Cetak saldo user")
        print("4. Top up saldo user")
        print("5. Booking hotel")
        print("6. Cetak nama user yang pernah melakukan booking pada hotel")
        print("7. Cetak nama hotel yang pernah di-booking oleh user")
        print("8. Keluar dari program Paciloka")

        command = int(input("Masukkan perintah: "))

        if command == 1:
            print("\nDaftar Hotel:")
            for hotel in hotels:
                print(f"{hotel.name}")
            print("\nDaftar User:")
            for user in users:
                print(f"{user.name}")

        elif command == 2:
            hotel_name = input("Masukkan nama hotel: ")
            found_hotel = find_hotel(hotels, hotel_name)
            if found_hotel:
                print(f"Hotel dengan nama {hotel_name} mempunyai profit sebesar {found_hotel.profit}")
            else:
                print(f"Error: Hotel dengan nama {hotel_name} tidak ditemukan!")

        elif command == 3:
            user_name = input("Masukkan nama user: ")
            found_user = find_user(users, user_name)
            if found_user:
                print(f"User dengan nama {user_name} mempunyai saldo sebesar {found_user.money}")
            else:
                print(f"Error: User dengan nama {user_name} tidak ditemukan!")

        elif command == 4:
            user_name = input("Masukkan nama user: ")
            found_user = find_user(users, user_name)
            if found_user:
                amount = int(input("Masukkan jumlah uang yang akan ditambahkan ke user: "))
                if amount > 0:
                    found_user.topup(amount)
                else:
                    print("Jumlah saldo yang akan ditambahkan ke user harus lebih dari 0!")
            else:
                print(f"Error: User dengan nama {user_name} tidak ditemukan!")

        elif command == 5:
            user_name = input("Masukkan nama user: ")
            hotel_name = input("Masukkan nama hotel: ")
            found_user = find_user(users, user_name)
            found_hotel = find_hotel(hotels, hotel_name)
            if found_user and found_hotel:
                num_rooms = int(input("Masukkan jumlah kamar yang akan dibooking: "))
                found_hotel.booking(found_user, num_rooms)
            else:
                print("Error: Nama user atau nama hotel tidak ditemukan!")

        elif command == 6:
            hotel_name = input("Masukkan nama hotel: ")
            found_hotel = find_hotel(hotels, hotel_name)
            if found_hotel:
                guests = found_hotel.get_guests()
                if guests:
                    print(f"{found_hotel}\n")
                else:
                    print(f"Hotel {hotel_name} tidak memiliki pelanggan!")
            else:
                print(f"Error: Hotel dengan nama {hotel_name} tidak ditemukan!")

        elif command == 7:
            user_name = input("Masukkan nama user: ")
            found_user = find_user(users, user_name)
            if found_user:
                booked_hotels = found_user.get_booked_hotels()
                if booked_hotels:
                    print(f"{found_user}\n")
                else:
                    print(f"{user_name} tidak pernah melakukan booking!")
            else:
                print(f"Error: User dengan nama {user_name} tidak ditemukan!")

        elif command == 8:
            print("Terima kasih sudah mengunjungi Paciloka!")
            break

        else:
            print("Perintah tidak diketahui! Masukkan perintah yang valid")


if __name__ == "__main__":
    main()
```

