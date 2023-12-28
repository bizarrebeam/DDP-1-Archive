# Kolaborator: Nasha Zahira (2306165553)

class Hotel:
    def __init__(self, name, available_room, room_price):
        self.name = name
        self.available_room = available_room
        self.room_price = room_price

        # Initial variables
        self.profit = 0
        self.guest = []

    # Method to proceed booking
    def booking(self, user, num_rooms):
        if self.available_room >= num_rooms and num_rooms > 0:
            cost = num_rooms * self.room_price

            # Proceed if user's balance could affor the room's price
            if user.money >= cost:
                user.money -= cost
                self.profit += cost
                self.available_room -= num_rooms

                # Add user's booking history to the guest data
                if user.name not in self.guest:
                    self.guest.append(user.name)

                # Add user's booking history to the hotel data
                if self.name not in user.hotel_list:
                    user.hotel_list.append(self.name)

                print(
                    f"User dengan nama {user.name} berhasil melakukan booking di hotel {self.name} dengan jumlah {num_rooms} kamar!"
                    )
            
            else:
                print(
                    f"{user.name} tidak memiliki cukup saldo untuk melakukan booking."
                    )
        
        else:
            if num_rooms <= 0:
                print(
                    "Jumlah kamar yang akan dipesan harus lebih dari 0!"
                    )
            else:
                print(
                    "Booking tidak berhasil karena melebihi jumlah kamar yang tersedia!"
                    )
    
    # Get the guest data list
    def get_guests(self):
        return self.guest

    # Get the history of the users that have made a booking at the hotel
    def __str__(self):
        return f"{self.name} | {', '.join(self.guest)}"

class User:
    def __init__(self, name, money):
        self.name = name
        self.money = money

        # Initial variables 
        self.hotel_list = []

    # Proceed top up mechanism if the number input is valid
    def topup(self, amount):
        if amount > 0:
            self.money += amount
            print(
                f"Berhasil menambahkan {amount} ke user {self.name}. Saldo user menjadi {self.money}"
                )

        else:
            print(
                "Jumlah saldo yang akan ditambahkan ke user harus lebih dari 0!"
                )

    # Get the booked hotels list
    def get_booked_hotels(self):
        return self.hotel_list

    # Get all the hotel names that have been booked by user
    def __str__(self):
        return f"{self.name} | {', '.join(self.hotel_list)}"

# Main interface to process the loop
def main():
    num_hotels = int(input("Masukkan banyak hotel: "))
    num_users = int(input("Masukkan banyak user: "))

    # Initial variables
    hotels = []
    users = []

    # Get the initial hotel's data 
    for i in range(1, num_hotels + 1):
        name = input(f"\nMasukkan nama hotel ke-{i}: ")
        rooms = int(input(f"Masukkan banyak kamar hotel ke-{i}: "))
        price = int(input(f"Masukkan harga satu kamar hotel ke-{i}: "))

        hotel = Hotel(name, rooms, price)
        hotels.append(hotel)

    # Get the initial user's data
    for i in range(1, num_users + 1):
        name = input(f"\nMasukkan nama user ke-{i}: ")
        balance = int(input(f"Masukkan saldo user ke-{i}: "))

        user = User(name, balance)
        users.append(user)

    # Loop to process each action
    while True:
        print("\n=============Welcome to Paciloka!=============\n")
        action = input("Masukkan nomor aksi (1-8): ")

        # 1: Print all the hotel and user names in the system
        if action == "1":
            print("Daftar Hotel:")
            for i, hotel in enumerate(hotels, 1):
                print(f"{i}. {hotel.name}\n")

            print("Daftar User:")
            for j, user in enumerate(users, 1):
                print(f"{j}. {user.name}")

        # 2: Print a hotel's profit 
        elif action == "2":
            hotel_name = input("Masukkan nama hotel: ")
            found_hotel = None # Track the match of hotel input and system's data

            for hotel in hotels:
                if hotel.name == hotel_name:
                    found_hotel = hotel
                    break

            if found_hotel:
                print(
                    f"Hotel dengan nama {found_hotel.name} mempunyai profit sebesar {found_hotel.profit}"
                    )
            else:
                print(
                    f"Hotel dengan nama {hotel_name} tidak ditemukan."
                    )

        # 3: Check user's balance
        elif action == "3":
            user_name = input("Masukkan nama user: ")
            found_user = None   # Track the match of user input and system's data

            for user in users:
                if user.name == user_name:
                    found_user = user
                    break

            if found_user:
                print(
                    f"User dengan nama {found_user.name} mempunyai saldo sebesar {found_user.money}"
                    )

            else:
                print(
                    f"Nama {user_name} tidak ditemukan di sistem!"
                    )

        # User want to top up an amount of money to its balance 
        elif action == "4":
            user_name = input("Masukkan nama user: ")
            found_user = None # Track the match of user input and system's data

            for user in users:
                if user.name == user_name:
                    found_user = user
                    break

            if found_user:
                # Validating the 'amount of money' input
                try:
                    amount = int(input("Masukkan jumlah saldo yang akan ditambahkan: "))
                    found_user.topup(amount)
                except ValueError:
                    print("Masukkan jumlah saldo yang valid (angka).")

            else:
                print(f"Nama {user_name} tidak ditemukan di sistem!")

        # 5: User want to booking a hotel room
        elif action == "5":
            user_name = input("Masukkan nama user: ")
            found_user = None # Track the match of user input and system's data

            for user in users:
                if user.name == user_name:
                    found_user = user
                    break

            if found_user:
                hotel_name = input("Masukkan nama hotel: ")
                found_hotel = None # Track the match of hotel name input and system's data

                for hotel in hotels:
                    if hotel.name == hotel_name:
                        found_hotel = hotel
                        break

                if found_hotel:
                    # Validating the 'number of room booked' input
                    try:
                        num_rooms = int(input(
                            "Masukkan jumlah kamar yang akan dibooking: "
                            ))
                        found_hotel.booking(found_user, num_rooms)
                    except ValueError:
                        print("Masukkan jumlah kamar yang valid (angka).")

                else:
                    print(f"Hotel {hotel_name} tidak ditemukan di sistem!")

            else:
                print(f"Nama {user_name} tidak ditemukan di sistem!")

        # 6: Print the history of the users have made a booking at the hotel        
        elif action == "6":
            hotel_name = input("Masukkan nama hotel: ")
            found_hotel = None # Track the match of hotel name input and system's data

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
                print(f"Hotel dengan nama {hotel_name} tidak ditemukan.")
        
        # 7: Print all the hotel names that have been booked by user
        elif action == "7":
            user_name = input("Masukkan nama user: ")
            found_user = None # Track the match of user input and system's data

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
                print(f"User dengan nama {user_name} tidak ditemukan di sistem.")

        # 8: Exit the program
        elif action == "8":
            print("Terima kasih sudah mengunjungi Paciloka!")
            break

        # Handles invalid action
        else:
            print("Perintah tidak diketahui! Masukkan perintah yang valid")

if __name__ == "__main__":
    main()
