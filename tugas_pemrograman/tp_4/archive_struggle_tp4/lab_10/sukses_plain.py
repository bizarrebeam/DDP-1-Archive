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
        self.homepage()
        
    def homepage(self):
        self.label_vars = []

        for hotel in self.hotels:
            label_var = tk.StringVar()
            label_var.set(f"\nHotel: {hotel.name}\nAvailable Rooms: {hotel.available_rooms}\nRoom Price: {hotel.room_price}\n")
            self.label_vars.append(label_var)
            
            tk.Label(self.master, textvariable=label_var).pack()

        tk.Label(self.master, text='Username:').pack()
        self.entry_username = tk.Entry(self.master)
        self.entry_username.pack()

        tk.Label(self.master, text='Hotel Name:').pack()
        self.entry_hotel_name = tk.Entry(self.master)
        self.entry_hotel_name.pack()

        tk.Label(self.master, text='Number of Rooms:').pack()
        self.entry_num_of_rooms = tk.Entry(self.master)
        self.entry_num_of_rooms.pack()

        tk.Button(self.master, text='Book Now!', command=self.booking).pack()

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

                # Update the label for the selected hotel
                index = self.hotels.index(selected_hotel)
                self.label_vars[index].set(f"\nHotel: {selected_hotel.name}\nAvailable Rooms: {selected_hotel.available_rooms}\nRoom Price: {selected_hotel.room_price}\n")

                ticket_number = f"{selected_hotel.hotel_code}/{selected_hotel.available_rooms}/{username[:3].lower()}"
                messagebox.showinfo("We got your room!", f"Booking Successful!\nOrder for {username} at {hotel_name} for {num_of_rooms} rooms!\nTotal Cost: {total_cost}\nTicket Number: {ticket_number}")
            else:
                messagebox.showerror("We can't yet get the room..", f"Sorry, unable to book {num_of_rooms} rooms at {hotel_name}.")
        else:   
            messagebox.showerror("Invalid input :(", f"Sorry, {hotel_name} is not available in the system.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PacilokaApp(master=root)
    root.mainloop()
