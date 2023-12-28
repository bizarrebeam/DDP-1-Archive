
class Person:
    def __init__(self, name, payment, stamina):                                    
        self.__name = name                                                         # Set Person's class attribute
        self.__payment = payment
        self.__stamina = stamina
        self.__total_work = 0

    def get_name(self):                                                            # Getter name
        return self.__name.lower()

    def get_payment(self):                                                         # Getter payment
        return self.__payment

    def get_stamina(self):                                                         # Getter stamina
        return self.__stamina

    def get_total_work(self):                                                      # Getter total work
        return self.__total_work

    def set_stamina(self, i):                                                      # Setter stamina
        self.__stamina = i

    def set_total_work(self, i):                                                   # Setter total work
        self.__total_work = i

    def pay_day(self):                                                             # Calculate payment
        return self.__payment * self.__total_work

    def is_available(self, cost_stamina):                                          # Check whether a work is available    
        return self.__stamina >= cost_stamina                                         # based on  worker's stamina state

    def work(self, cost_stamina):                                                  # If work is available, decrement the stamina
        if self.is_available(cost_stamina):
            self.__stamina -= cost_stamina
            self.__total_work += 1
            return True
        
        return False

    def __str__(self):                                                             # Str representation for Person's Class                                        
        class_name = self.__class__.__name__
        total_payment = self.pay_day()

        return f"{class_name:20} | {self.__name.title():20} | Total kerja: "\
            f"{self.__total_work:20} | Stamina:{self.__stamina:20} | "\
                f"Gaji:{total_payment:20}"

class Worker(Person):
    def __init__(self, name, payment=5000, stamina=100):                           # Set Worker's Class attribute
        super().__init__(name, payment, stamina)                                   # Inherit Person Class attribute
        self.__bonus = 0

    def work(self, bonus, cost_stamina):                                           # Accumulate bonus if work taken
        if super().work(cost_stamina):
            self.__bonus += bonus
            return True
        
        return False
    
    def pay_day(self):
        return super().pay_day() + self.__bonus                                    # Accumulate bonus

    def get_bonus(self):                                                           # Bonus getter
        return self.__bonus

    def set_bonus(self, new_bonus):                                                # Bonus setter
        self.__bonus = new_bonus

class Manager(Person):
    def __init__(self, name, payment, stamina):                                    # Set Manager's class attribute
        super().__init__(name, payment, stamina)                                   # Inherit Person Class attribute
        self.__list_worker = []                                                    # Initialize empty workers list

    def get_list_worker(self):                                                     # Getter worker list                                           
        return self.__list_worker

    def hire_worker(self, name):                                                   # Recruit new worker
        worker_names = [worker.get_name() for worker in self.__list_worker]        # Add to the worker list

        if name.lower() not in worker_names:                                       # Process only unique worker name
            self.__list_worker.append(Worker(name, payment=5000, stamina=100))        # (not the ones already on the list)
            self.set_stamina(self.get_stamina() - 10)
            self.set_total_work(self.get_total_work() + 1)
            print(f"Berhasil mendapat pegawai baru")
            
        else:
            print(f"Sudah ada!")

    def fire_worker(self, name):                                                   # Fire the worker
        for worker in self.__list_worker:                                   
            if worker.get_name() == name.lower():                                  # Process only unique worker name
                self.__list_worker.remove(worker)                                    # (not the ones already on the list)
                self.set_stamina(self.get_stamina() - 10)
                self.set_total_work(self.get_total_work() + 1)
                print(f"Berhasil memecat {name}")
                return
            
        else:
            print(f"Nama tidak ditemukan")

    def give_work(self, name, bonus, cost_stamina):                                # Give a work 
        for worker in self.__list_worker:
            if worker.get_name() == name.lower():                                  # Process only for existing worker

                if worker.work(bonus, cost_stamina):                                 # with enough amount of stamina
                    self.set_stamina(self.get_stamina() - 10)
                    self.set_total_work(self.get_total_work() + 1)
                    print(f"Hasil cek ketersediaan pegawai:\nPegawai "\
                          f"dapat menerima pekerjaan\n{'=' * 40}"
                    )   
                    print(
                        f"Berhasil memberi pekerjaan kepada {name}"
                        )

                else:
                    print(
                        f"Hasil cek ketersediaan pegawai:\nPegawai tidak dapat "\
                        f"menerima pekerjaan.\n{'=' * 40}"
                    )
                    print(
                        "Stamina pegawai tidak cukup."
                    )

                return
            
        else:
            print(
                f"Hasil cek ketersediaan pegawai:\nPegawai dengan nama {name} "\
                f"tidak ditemukan.\n{'=' * 40}"
            )
            print(
                f"Pegawai dengan nama {name} tidak ditemukan."
                )
    
    def __str__(self):                                                            # Str representation of Manager's class
        class_name = self.__class__.__name__
        total_payment = self.pay_day()
        
        return f"{class_name:20} | {self.get_name().title():20} | Total kerja: "\
            f"{self.get_total_work():20} | Stamina:{self.get_stamina():20} | "\
                f"Gaji:{total_payment:20}\n"
    
def main():                                                                       # Func to executes the main program
    name = input("Masukkan nama manajer: ")                                       # Input initial values
    payment = int(input("Masukkan jumlah pembayaran: "))
    stamina = int(input("Masukkan stamina manajer: "))

    manager = Manager(name, payment, stamina)

    while manager.is_available(1):                                                # Loop for the main program
        print("""
PACILOKA
-----------------------
1. Lihat status pegawai
2. Beri tugas
3. Cari pegawai baru
4. Pecat pegawai
5. Keluar
-----------------------
        """)
        action = int(input("Masukkan pilihan: "))

        if action == 1:                                                          # Print the manager and the worker name
            print(manager) 
            for worker in manager.get_list_worker():
                print(worker)

        elif action == 2:                                                        # Give work to a worker
            worker_name = input("Tugas akan diberikan kepada: ")                  # then accumulate bonus and cost stamina
            bonus = int(input("Bonus pekerjaan: "))
            cost_stamina = int(input("Beban stamina: "))

            manager.give_work(worker_name, bonus, cost_stamina)

        elif action == 3:                                                        # Hire and add a new worker
            worker_name = input("Nama pegawai baru: ")
            manager.hire_worker(worker_name)

        elif action == 4:                                                        # Fire a worker
            worker_name = input("Nama pegawai yang akan dipecat: ")
            manager.fire_worker(worker_name)

        elif action == 5:                                                        # Exit the program
            print("""
----------------------------------------
Berhenti mengawasi hotel, sampai jumpa !
----------------------------------------""")
            return

    print("""
----------------------------------------
Stamina manajer sudah habis, sampai jumpa !
----------------------------------------""")


if __name__ == "__main__":
    main()
