class Hotel:
    def __init__(self, name, available_room, room_price):
        self.name = name
        self.available_room = available_room
        self.room_price = room_price
        self.profit = 0
        self.guest = []

    def booking(self, user, num_rooms):
        if self.available_room >= num_rooms and num_rooms > 0:
            cost = num_rooms * self.room_price
            if user.money >= cost:
                user.money -= cost
                self.profit += cost
                self.available_room -= num_rooms
                self.guest.append(user.name)
                if user.name not in self.guest:
                    self.guest.append(user.name)
                if self.name not in user.hotel_list:
                    user.hotel_list.append(self.name)
                print(f"User dengan nama {user.name} berhasil melakukan booking di hotel {self.name} dengan jumlah {num_rooms} kamar!")
            else:
                print(f"Error: {user.name} tidak memiliki cukup saldo untuk melakukan booking.")
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


def main():
    num_hotels = int(input("Masukkan banyak hotel: "))
    num_users = int(input("Masukkan banyak user: "))

    hotels = []
    users = []

    for i in range(num_hotels):
        name = input(f"Masukkan nama hotel ke-{i + 1}: ")
        rooms = int(input(f"Masukkan banyak kamar hotel ke-{i + 1}: "))
        price = int(input(f"Masukkan harga satu kamar hotel ke-{i + 1}: "))
        hotel = Hotel(name, rooms, price)
        hotels.append(hotel)

    for i in range(num_users):
        name = input(f"Masukkan nama user ke-{i + 1}: ")
        balance = int(input(f"Masukkan saldo user ke-{i + 1}: "))
        user = User(name, balance)
        users.append(user)

    print("\n=============Welcome to Paciloka!=============")

    while True:
        print("\nMasukkan perintah :")
        print("1. Daftar Hotel")
        print("2. Daftar User")
        print("3. Cetak profit dari sebuah hotel")
        print("4. Cetak saldo user")
        print("5. Booking hotel oleh user")
        print("6. Cetak semua user yang pernah melakukan booking pada hotel")
        print("7. Cetak semua hotel yang pernah di-booking oleh user")
        print("8. Keluar dari program Paciloka")

        command = input("Masukkan nomor perintah (0-8): ")

        if command == "1":
            for hotel in hotels:
                print(hotel)

        elif command == "2":
            for user in users:
                print(user)

        elif command == "3":
            hotel_name = input("Masukkan nama hotel: ")
            found_hotel = None
            for hotel in hotels:
                if hotel.name == hotel_name:
                    found_hotel = hotel
                    break
            if found_hotel:
                print(f"Hotel dengan nama {found_hotel.name} mempunyai profit sebesar {found_hotel.profit}")
            else:
                print(f"Error: Hotel dengan nama {hotel_name} tidak ditemukan.")

        elif command == "4":
            user_name = input("Masukkan nama user: ")
            found_user = None
            for user in users:
                if user.name == user_name:
                    found_user = user
                    break
            if found_user:
                print(f"User dengan nama {found_user.name} mempunyai saldo sebesar {found_user.money}")
            else:
                print(f"Error: User dengan nama {user_name} tidak ditemukan.")

        elif command == "5":
            user_name = input("Masukkan nama user: ")
            hotel_name = input("Masukkan nama hotel: ")
            found_user = None
            found_hotel = None
            for user in users:
                if user.name == user_name:
                    found_user = user
                    break
            for hotel in hotels:
                if hotel.name == hotel_name:
                    found_hotel = hotel
                    break
            if found_user and found_hotel:
                try:
                    num_rooms = int(input("Masukkan jumlah kamar yang akan dibooking: "))
                    found_hotel.booking(found_user, num_rooms)
                except ValueError:
                    print("Error: Masukkan jumlah kamar yang valid (angka).")
            else:
                print(f"Error: User dengan nama {user_name} atau Hotel dengan nama {hotel_name} tidak ditemukan.")

        elif command == "6":
            hotel_name = input("Masukkan nama hotel: ")
            found_hotel = None
            for hotel in hotels:
                if hotel.name == hotel_name:
                    found_hotel = hotel
                    break
            if found_hotel:
                guests = found_hotel.get_guests()
                if guests:
                    print(f"{found_hotel}")
                else:
                    print(f"Hotel {found_hotel.name} tidak memiliki pelanggan!")
            else:
                print(f"Error: Hotel dengan nama {hotel_name} tidak ditemukan.")

        elif command == "7":
            user_name = input("Masukkan nama user: ")
            found_user = None
            for user in users:
                if user.name == user_name:
                    found_user = user
                    break
            if found_user:
                booked_hotels = found_user.get_booked_hotels()
                if booked_hotels:
                    print(f"{found_user}")
                else:
                    print(f"User {found_user.name} tidak pernah melakukan booking!")
            else:
                print(f"Error: User dengan nama {user_name} tidak ditemukan.")

        elif command == "8":
            print("Terima kasih sudah mengunjungi Paciloka! 😢")
            break

        else:
            print("Perintah tidak diketahui! Masukkan perintah yang valid")

if __name__ == "__main__":
    main()
