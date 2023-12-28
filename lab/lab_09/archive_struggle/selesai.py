from random import randint


class Person:

    def __init__(self, name, payment, stamina):
        self.__name = name
        self.__payment = payment
        self.__stamina = stamina
        self.__total_work = 0

    def get_name(self):
        return self.__name.lower()

    def get_payment(self):
        return self.__payment

    def get_stamina(self):
        return self.__stamina
    
    def get_total_work(self):
        return self.__total_work
    
    def set_stamina(self, i):
        self.__stamina = i

    def set_total_work(self, i):
        self.__total_work = i

    def pay_day(self):
        return self.__payment * self.__total_work
    
    def is_available(self, cost_stamina):
        return self.__stamina >= cost_stamina

    def work(self, cost_stamina):
        if self.is_available(cost_stamina):
            self.__stamina -= cost_stamina
            self.__total_work += 1
            return True
        return False

    def __str__(self):
        class_name = self.__class__.__name__
        return f"{class_name:20} | {self.__name:20} | Total kerja: {self.__total_work:20} | Stamina:{self.__stamina:20} | Gaji:{self.__payment:20}"

class Worker(Person):

    def __init__(self, name, payment = 5000, stamina = 100 ):
        super().__init__(name, payment, stamina)
        self.__bonus = 0

    def work(self, bonus, cost_stamina):
        if super().work(cost_stamina):
            self.__bonus += bonus
            return True
        return False
    
    def get_bonus(self):
        return self.__bonus
    
    def set_bonus(self, new_bonus):
        self.__bonus = new_bonus


class Manager(Person):
    
    def __init__(self, name, payment, stamina):
        super().__init__(name, payment, stamina)
        self.__list_worker = []
        
    def get_list_worker(self):
        return self.__list_worker

    def hire_worker(self, name):
        worker_names = [worker.name for worker in self.__list_worker]

        if name.lower() not in worker_names:
            self.__list_worker.append(Worker(name, payment = 5000, stamina = 100))
            self.set_stamina(self.get_stamina() - 10)
            self.set_total_work(self.get_total_work() + 1)
            print(f"Berhasil mendapat pegawai baru: {name}")

        else:
            print(f"Pegawai dengan nama {name} sudah ada.")
        
    def fire_worker(self, name):
        for worker in self.__list_worker:
            if worker.name == name.lower():
                self.__list_worker.remove(worker)
                self.stamina -= 10
                self.total_work += 1
                print(f"{name} berhasil dipecat.")
                return
        else: 
            print(f"Pegawai dengan nama {name} tidak ditemukan.")

    def give_work(self, name,bonus ,cost_stamina):
        for worker in self.__list_worker:
            if worker.name == name.lower():
                if worker.work(bonus, cost_stamina):
                    self.stamina -= 10
                    self.total_work += 1
                    print(f"Berhasil memberi pekerjaan kepada {name}")
                else:
                    print(f"{name} tidak memiliki cukup stamina untuk tugas ini.")
                return
        else:  
            print(f"Pegawai dengan nama {name} tidak ditemukan.")


def main():

    name =  input("Masukkan nama manajer: ")
    payment = int(input("Masukkan jumlah pembayaran: "))
    stamina = int(input("Masukkan stamina manajer: "))

    manager = Manager(name, payment, stamina)

    while manager.is_available(1):
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
        
        if action == 1: 
            for worker in manager.get_list_worker():
                print(worker)

        elif action == 2:
            worker_name = input("Tugas akan diberikan kepada: ")
            bonus = int(input("Bonus pekerjaan: "))
            cost_stamina = int(input("Beban stamina: "))

            manager.give_work(worker_name, bonus, cost_stamina)

        elif action == 3:
            worker_name = input("Nama pegawai baru: ")
            manager.hire_worker(worker_name)

        elif action == 4:
            worker_name = input("Nama pegawai yang akan dipecat: ")
            manager.fire_worker(worker_name)

        elif action == 5:
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
