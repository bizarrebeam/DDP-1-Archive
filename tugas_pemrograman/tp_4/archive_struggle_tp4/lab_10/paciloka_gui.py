import tkinter as tk
from tkinter import messagebox

# Class to defined hotel's object
class Hotel:
    def __init__(self, name, available_rooms, room_price, hotel_code) -> None:
        self.name = name
        self.available_rooms = available_rooms
        self.room_price = room_price
        self.hotel_code = hotel_code

# Class for the main app interface and logic
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
        self.master.geometry('280x460')                               # Set the window's size
        self.homepage()                                               
    
    # Method to display the main widget (interface)
    def homepage(self):                                               
        tk.Label(self.master, text="Choose your own room!", font=("Helvetica bold white", 16), fg = 'white', bg = '#588157').grid(row=0, column=0, columnspan=2, pady=10)

        row_count = 1                                                 # Track the row of the grid
        col_count = 0                                                 # Track the column of the grid
        for hotel in self.hotels:                                     # The display of hotel's data is in 2X3 column (grid system)
            tk.Label(self.master, text=f"Hotel: {hotel.name}\nAvailable Rooms: {hotel.available_rooms}\nRoom Price: {hotel.room_price}\n", bg = '#dad7cd').grid(row=row_count, column=col_count, padx=10, pady=5)
            col_count += 1
            if col_count == 2:                                        # Two column for each row                             
                col_count = 0
                row_count += 1

        tk.Label(self.master, text='Username', bg = '#a3b18a').grid(row=row_count, column=0, pady=5, padx=10)                                          # Ask for username
        self.entry_username = tk.Entry(self.master)
        self.entry_username.grid(row=row_count, column=1, pady=5, padx=10)
        row_count += 1

        tk.Label(self.master, text='Hotel Name', bg = '#a3b18a').grid(row=row_count, column=0, pady=5, padx=10)                                        # Ask for hotel name to be booked
        self.entry_hotel_name = tk.Entry(self.master)
        self.entry_hotel_name.grid(row=row_count, column=1, pady=5, padx=10)
        row_count += 1

        tk.Label(self.master, text='Number of Rooms', bg = '#a3b18a').grid(row=row_count, column=0, pady=5, padx=10)                                   # Ask for number of rooms to be booked
        self.entry_num_of_rooms = tk.Entry(self.master)
        self.entry_num_of_rooms.grid(row=row_count, column=1, pady=5, padx=10)
        row_count += 1

        tk.Button(self.master, text='Book Now!', command=self.booking, bg = '#588157', fg = 'white').grid(row=row_count, column=0, columnspan=2, pady=10)             # Button to proceed booking
        tk.Button(self.master, text= "I'm done with my booking!", command=self.master.destroy, bg = '#588157', fg = 'white').grid(row=row_count + 1, column=0, columnspan=2, pady=10)       # Exit the main app

    # Method to proceed the booking system
    def booking(self):
        # Retrieve all the data from the entry
        username = self.entry_username.get()                                                                                            
        hotel_name = self.entry_hotel_name.get()
        input_num_of_rooms = self.entry_num_of_rooms.get()

        # Proceed only valid input for number of rooms and display error message if it's not valid
        try:
            num_of_rooms = int(input_num_of_rooms)                                          
            if num_of_rooms <= 0:
                messagebox.showerror("Invalid Input :(", "Number of rooms must be greater than 0")
                return
        except ValueError:
            messagebox.showerror("Invalid Input :(", "Number of rooms must be a positive integer")
            return
        
        # Match the hotel name from input with the existing data
        selected_hotel = None
        for hotel in self.hotels:
            if hotel.name.lower() == hotel_name.lower():
                selected_hotel = hotel
                break
        
        # If the hotel name match, proceed the booking and the total cost
        if selected_hotel:
            if num_of_rooms > 0 and num_of_rooms <= selected_hotel.available_rooms:
                total_cost = num_of_rooms * selected_hotel.room_price

                # Clear the entry for the next booking
                selected_hotel.available_rooms -= num_of_rooms
                self.entry_username.delete(0, tk.END)
                self.entry_hotel_name.delete(0, tk.END)
                self.entry_num_of_rooms.delete(0, tk.END)
                
                # Updating the hotel's data after rooms have been successfully booked
                index = self.hotels.index(selected_hotel)
                tk.Label(self.master, text=f"Hotel: {selected_hotel.name}\nAvailable Rooms: {selected_hotel.available_rooms}\nRoom Price: {selected_hotel.room_price}\n").grid(row=index // 2 + 1, column=index % 2, padx=10, pady=5)

                # Display info that the booking is successful
                ticket_number = f"{selected_hotel.hotel_code}/{selected_hotel.available_rooms}/{username[:3].lower()}"
                messagebox.showinfo("We got your room!", f"Booking Successful!\nOrder for {username} at {hotel_name} for {num_of_rooms} rooms! Total Cost: {total_cost}\nTicket Number: {ticket_number}")
            
            else:       
                messagebox.showerror("We can't yet get the room..", f"Sorry, unable to book {num_of_rooms} rooms at {hotel_name}.") # The number of room booked exceed the available room
        
        else:   
            messagebox.showerror("Invalid input :(", f"Sorry, {hotel_name} is not available in the system.")                        # The hotel name input doesn't exist in hotel database

if __name__ == "__main__":
    root = tk.Tk()
    app = PacilokaApp(master=root)
    root.mainloop()
