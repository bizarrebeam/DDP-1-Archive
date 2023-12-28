#Inisialisasi objek Hotel
class Hotel:
    def __init__(self, name, available_room, room_price):
        self.name = name
        self.available_room = available_room
        self.room_price = room_price
        self.profit = 0
        self.guest = []

#Proses pemesanan kamar hotel.
    def booking(self, user, num_rooms):
        if num_rooms > 0 and num_rooms <= self.available_room and user.money >= num_rooms * self.room_price:
            cost = num_rooms * self.room_price
            self.profit += cost
            user.money -= cost
            self.available_room -= num_rooms
            user.hotel_list.add(self.name)
            self.guest.append(user.name)
            return True
        else:
            return False
        
#Representasi string objek Hotel.
    def __str__(self):
        return f"{self.name}"

#Inisialisasi objek User
class User:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.hotel_list = set()

#Menambahkan saldo pengguna.
    def topup(self, amount):
        if amount > 0:
            self.money += amount
            return True
        else:
            return False

#Representasi string objek User
    def __str__(self):
        return f"{self.name}"

#Cetak daftar hotel dan pengguna.
def print_hotels_and_users(hotels, users):
    print("Daftar Hotel:")
    for i, hotel in enumerate(hotels, 1):
        print(f"{i}. {hotel}")

    print("\nDaftar Users:")
    for i, user in enumerate(users, 1):
        print(f"{i}. {user}")

#cetak profit hotel
def print_hotel_profit(hotels, hotel_name):
    for hotel in hotels:
        if hotel.name == hotel_name:
            print(f"Hotel dengan nama {hotel_name} mempunyai profit sebesar {hotel.profit} ")
            return
    print(f"Nama hotel tidak ditemukan di sistem!")

#Cetak saldo suatu user.
def print_user_balance(users, user_name):
    for user in users:
        if user.name == user_name:
            print(f"User dengan nama {user_name} mempunyai saldo sebesar {user.money}")
            return
    print(f"Nama user tidak ditemukan di sistem!")

#Top-up saldo suatu user.
def topup_user_balance(users, user_name, amount):
    for user in users:
        if user.name == user_name:
            if amount > 0:
                print(f"Berhasil menambahkan {amount} ke user {user_name}. Saldo user menjadi {user_money}")
        else:
            print("Jumlah saldo yang akan ditambahkan ke user harus lebih dari 0!")
    else:
        print(f"Nama user {user_name} tidak ditemukan di sistem!")

#Proses pemesanan kamar hotel oleh user.
def book_hotel(hotels, users, user_name, hotel_name, num_rooms):
    for user in users:
        if user.name == user_name:
            for hotel in hotels:
                if hotel.name == hotel_name:
                    if hotel.booking(user, num_rooms):
                        print(f"User dengan nama {user_name} berhasil melakukan booking di {hotel_name} dengan jumlah {num_rooms} kamar!")
                    else:
                        print("Booking tidak berhasil!")
                    return
                else:
                    print("Nama hotel tidak ditemukan di sistem!")
            print(f"Nama hotel tidak ditemukan di sistem!")
            return
    print(f"Nama user tidak ditemukan di sistem!")

#Cetak daftar pengguna yang melakukan pemesanan di suatu hotel.
def print_users_at_hotel(hotels, hotel_name):
    for hotel in hotels:
        if hotel.name == hotel_name:
            if len(hotel.guest) > 0:
                print(f"{hotel_name} | {', '.join(hotel.guest)}")
            else:
                print(f"Hotel {hotel_name} tidak memiliki pelanggan!")
            return
    print(f"Nama hotel tidak ditemukan di sistem!")

#Cetak daftar hotel yang pernah dipesan oleh user.
def print_hotels_booked_by_user(users, user_name):
    for user in users:
        if user.name == user_name:
            if len(user.hotel_list) > 0:
                print(f"{user_name} | {', '.join(user.hotel_list)}")
            else:
                print(f"User {user_name} tidak pernah melakukan booking!")
            return
    print(f"Nama user tidak ditemukan di sistem!")

# Program starts here
num_hotels = int(input("Masukkan banyak hotel : "))
num_users = int(input("Masukkan banyak user : "))
print("")
hotels = []
users = []

for i in range(num_hotels):
    hotel_name = input(f"Masukkan nama hotel ke-{i+1} : ")
    available_room = int(input(f"Masukkan banyak kamar hotel ke-{i+1} : "))
    room_price = int(input(f"Masukkan harga satu kamar hotel ke-{i+1} : "))
    hotels.append(Hotel(hotel_name, available_room, room_price))
print("")
for i in range(num_users):
    user_name = input(f"Masukkan nama user ke-{i+1} : ")
    user_money = int(input(f"Masukkan saldo user ke-{i+1} : "))
    users.append(User(user_name, user_money))
print("")
while True:
    print("\n=============Welcome to Paciloka!=============")
    print("")

    choice = input("Masukkan perintah : ")
   
    if choice == 1:
        print_hotels_and_users(hotels, users)
    elif choice == 2:
        hotel_name = input("Masukkan nama hotel : ")
        print_hotel_profit(hotels, hotel_name)
    elif choice == 3:
        user_name = input("Masukkan nama user : ")
        print_user_balance(users, user_name)
    elif choice == 4:
            user_name = input("Masukkan nama user: ")
            found_user = next((user for user in users if user.name == user_name), None)
            if found_user:
                amount = int(input("Masukkan jumlah uang yang akan ditambahkan ke user: "))
                if found_user.topup(amount):
                    print(f"Berhasil menambahkan {amount} ke user {found_user.name}. Saldo user menjadi {found_user.money}")
                else:
                    print("Jumlah saldo yang akan ditambahkan ke user harus lebih dari 0!")
            else:
                print(f"User dengan nama {user_name} tidak ditemukan!")

    elif choice == "5":
            # Membooking hotel
            user_name = input("Masukkan nama user: ")
            found_user = None

            for user in users:
                if user.name == user_name:
                    found_user = user
                    break

            if found_user:
                hotel_name = input("Masukkan nama hotel: ")
                found_hotel = None

                for hotel in hotels:
                    if hotel.name == hotel_name:
                        found_hotel = hotel
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
    elif choice == "6":
            hotel_name = input("Masukkan nama hotel: ")
            found_hotel = next((hotel for hotel in hotels if hotel.name == hotel_name), None)
            if found_hotel:
                if found_hotel.guest:
                    print(f"{found_hotel} | {', '.join(hotel.guest)}")
                else:
                    print(f"Hotel {found_hotel.name} tidak memiliki pelanggan!")
            else:
                print(f"Hotel dengan nama {hotel_name} tidak ditemukan!")

    elif choice == "7":
            user_name = input("Masukkan nama user: ")
            found_user = next((user for user in users if user.name == user_name), None)
            if found_user:
                if found_user.hotel_list:
                    print(f"{found_user} | {', '.join(hotel.guest)}")
                else:
                    print(f"User {found_user.name} tidak pernah melakukan booking!")
            else:
                print(f"User dengan nama {user_name} tidak ditemukan!")
    
    elif choice == 8:
        print("Terima kasih sudah mengunjungi Paciloka!")
        break
    else:
        print("Perintah tidak diketahui! Masukkan perintah yang valid")