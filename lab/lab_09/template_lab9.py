from random import randint


class Person:
    # TODO: Lengkapi constructor
    #       Perhatikan access modifiernya!
    def __init__(self, name, payment, stamina):
        ...

    # TODO: Lengkapi getter dan setter

    # TODO: Lengkapi method di bawah ini
    def is_available(self,cost_stamina):
        ...

    def pay_day(self):
        ...

    def work(self, cost_stamina):
        ...
    
    def __str__(self):
        # TODO
        ...

        return f"{class_name:20} | {name:20} | Total kerja: {total_work:20} | Stamina:{stamina:20} | Gaji:{payment:20}"


class Manager(Person):
    # TODO: Lengkapi constructor
    def __init__(self, name, payment, stamina):
        ...
        
    # Lengkapi getter dan setter
    def get_list_worker(self):
        ...

    # TODO: Lengkapi method berikut
    def hire_worker(self, name):
        ...
        
    def fire_worker(self, name):
        ...


    def give_work(self, name,bonus ,cost_stamina):
        ...


class Worker(Person):
    # TODO: Lengkapi constructor
    #       Perhatikan access modifiernya!
    def __init__(self, name, payment, stamina):
        ...

    # TODO: Lengkapi method berikut
    def work(self, bonus,cost_stamina):
        ...

    def get_bonus(self):
        return self.__bonus

    def set_bonus(self, new_bonus):
        self.__bonus = new_bonus    
    

def main():
    # TODO: meminta nama
    name =  input("Masukkan nama manajer: ")
    payment = int(input("Masukkan jumlah pembayaran: "))
    stamina = int(input("Masukkan stamina manajer: "))

    # TODO: Inisialisasi Manager
    manager = ...

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
        
        # TODO
        if action == 1:
            ...

        elif action == 2:
            ...

        elif action == 3:
            ...

        elif action == 4:
            ...

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
