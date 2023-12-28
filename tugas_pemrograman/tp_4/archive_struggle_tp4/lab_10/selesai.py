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
        self.dict_hotel = {
            'hotel1': [10, 250000, 'kode_hotel_1'], 
            'hotel2': [12, 500000, 'kode_hotel_2'], 
            'hotel3': [10, 7500000, 'kode_hotel_3'], 
            'hotel4': [1, 1000000, 'kode_hotel_4'], 
            'hotel5': [10, 900000, 'kode_hotel_5'], 
            'hotel6': [10, 6000000, 'kode_hotel_6']
            }
        
        self.master.title('Paciloka.com')
        self.master.geometry('400x500')
        self.homepage()
        
    def homepage(self):
        tk.Label(self.master, text="Get your holiday easy with Paciloka!").pack()

        for hotel in self.dict_hotel:
            tk.Label(self.master, text=f"\nHotel: {hotel.name}\nAvailable Rooms: {hotel.available_rooms}\nRoom Price: {hotel.room_price}\n").pack()

        tk.Label(self.master, text = 'Username:').pack()
        self.entry_username = tk.Entry(self.master).pack()

        tk.Label(self.master, text = 'Hotel Name:').pack()
        self.entry_hotel_name = tk.Entry(self.master).pack()

        tk.Label(self.master, text = 'Number of Rooms:').pack()
        self.entry_num_of_rooms = tk.Entry(self.master).pack()

        tk.Button(self.master, text = 'Book Now!', command = self.booking)

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
            if hotel['hotel_name'].lower() == hotel_name.lower():
                selected_hotel = hotel
                break
        
        if selected_hotel:
            if num_of_rooms > 0 and num_of_rooms <= selected_hotel.available_rooms:
                total_cost = num_of_rooms * selected_hotel.room_price

                selected_hotel.available_rooms -= num_of_rooms
                self.entry_username.delete(0, tk.END)
                self.entry_hotel_name.delete(0, tk.END)
                self.entry_num_of_rooms.delete(0, tk.END)

                ticket_number = f"{selected_hotel.hotel_code}/{selected_hotel.available_rooms}/{username[:3].lower()}"
                messagebox.showinfo("We got your room!", f"Booking Successful!\nOrder for {username} at {hotel_name} for {num_of_rooms} rooms! Total Cost: {total_cost}\nTicket Number: {ticket_number}")
            else:
                messagebox.showerror("We can't yet get the room..", f"Sorry, unable to book {num_of_rooms} rooms at {hotel_name}.")
        else:   
            messagebox.showerror("Invalid input :(", f"Sorry, {hotel_name} is not available in the system.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PacilokaApp(master=root)
    root.mainloop()

