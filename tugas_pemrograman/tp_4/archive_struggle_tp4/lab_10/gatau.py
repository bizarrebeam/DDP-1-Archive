import tkinter as tk
from tkinter import messagebox

class Hotel:
    def __init__(self, name, available_rooms, room_price, hotel_code) -> None:
        self.name = name
        self.available_rooms = available_rooms
        self.room_price = room_price
        self.hotel_code = hotel_code

class PacilokaApp:
    def __init__(self, master=None):
        self.master = master
        self.hotels = [
            Hotel('hotel1', 10, 250000, 'hotel_code_1'), 
            Hotel('hotel2', 12, 500000, 'hotel_code_2'), 
            Hotel('hotel3', 10, 7500000, 'hotel_code_3'), 
            Hotel('hotel4', 1, 1000000, 'hotel_code_4'), 
            Hotel('hotel5', 10, 900000, 'hotel_code_5'), 
            Hotel('hotel6', 10, 6000000, 'hotel_code_6')
        ]
        
        self.master.title('Get your holiday easy with Paciloka!')
        self.master.geometry('280x490') 
        self.homepage()
        
    def homepage(self):
        tk.Label(self.master, text="Choose your own room!", font=("Helvetica bold", 16)).grid(row=0, column=0, columnspan=2, pady=10)

        row_count = 1
        col_count = 0
        self.hotel_labels = []
        for hotel in self.hotels:
            hotel_label = tk.Label(self.master, text=f"Hotel: {hotel.name}\nAvailable Rooms: {hotel.available_rooms}\nRoom Price: {hotel.room_price}\n", anchor='w')
            hotel_label.grid(row=row_count, column=col_count, sticky="w", padx=10, pady=5)
            self.hotel_labels.append(hotel_label)
            col_count += 1
            if col_count == 2:
                col_count = 0
                row_count += 1

        tk.Label(self.master, text='Username:').grid(row=row_count, column=0, pady=5, padx=10)
        self.entry_username = tk.Entry(self.master)
        self.entry_username.grid(row=row_count, column=1, pady=5, padx=10)
        row_count += 1

        tk.Label(self.master, text='Hotel Name:').grid(row=row_count, column=0, pady=5, padx=10)
        self.entry_hotel_name = tk.Entry(self.master)
        self.entry_hotel_name.grid(row=row_count, column=1, pady=5, padx=10)
        row_count += 1

        tk.Label(self.master, text='Number of Rooms:').grid(row=row_count, column=0, pady=5, padx=10)
        self.entry_num_of_rooms = tk.Entry(self.master)
        self.entry_num_of_rooms.grid(row=row_count, column=1, pady=5, padx=10)
        row_count += 1

        tk.Button(self.master, text='Book Now!', command=self.booking).grid(row=row_count, column=0, columnspan=2, pady=10)
        tk.Button(self.master, text='Exit', command=self.master.destroy).grid(row=row_count + 1, column=0, columnspan=2, pady=10)

    def booking(self):
        username = self.entry_username.get()
        hotel_name = self.entry_hotel_name.get()
        input_num_of_rooms = self.entry_num_of_rooms.get()

        try:
            num_of_rooms = int(input_num_of_rooms)
            if num_of_rooms <= 0:
                messagebox.showerror("Invalid Input :(", "Number of rooms must be greater than 0")
                return
        except ValueError:
            messagebox.showerror("Invalid Input :(", "Number of rooms must be a positive integer")
            return
        
        selected_hotel = None
        for hotel in self.hotels:
            if hotel.name.lower() == hotel_name.lower():
                selected_hotel = hotel
                break
        
        if selected_hotel:
            if num_of_rooms > 0 and num_of_rooms <= selected_hotel.available_rooms:
                total_cost = num_of_rooms * selected_hotel.room_price

                selected_hotel.available_rooms -= num_of_rooms
                self.entry_username.delete(0, tk.END)
                self.entry_hotel_name.delete(0, tk.END)
                self.entry_num_of_rooms.delete(0, tk.END)
                
                index = self.hotels.index(selected_hotel)
                booking_label = tk.Label(self.master, text=f"\nHotel: {selected_hotel.name}\nAvailable Rooms: {selected_hotel.available_rooms}\nRoom Price: {selected_hotel.room_price}\n", anchor='w')
                booking_label.grid(row=index // 2 + 1, column=index % 2, sticky="w", padx=10, pady=5)
                self.hotel_labels[index].grid_remove()

                ticket_number = f"{selected_hotel.hotel_code}/{selected_hotel.available_rooms}/{username[:3].lower()}"
                messagebox.showinfo("We got your room!", f"Booking Successful!\nOrder for {username} at {hotel_name} for {num_of_rooms} rooms! Total Cost: {total_cost}\nTicket Number: {ticket_number}")
            
            else:
                messagebox.showerror("We can't yet get the room..", f"Sorry, unable to book {num_of_rooms} rooms at {hotel_name}.")
        
        else:   
            messagebox.showerror("Invalid input :(", f"No such hotel found. Please try again.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PacilokaApp(master=root)
    root.mainloop()
