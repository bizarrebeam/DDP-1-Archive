class Person:
    # Konstruktor untuk menginisialisasi atribut Person
    def __init__(self, name, payment, stamina):
        self.__name = name
        self.__payment = payment
        self.__stamina = stamina
        self.__total_work = 0

    @property
    def name(self):
        return self.__name

    @property
    def payment(self):
        return self.__payment

    @property
    def stamina(self):
        return self.__stamina

    @property
    def total_work(self):
        return self.__total_work

    @stamina.setter
    def stamina(self, value):
        self.__stamina = value

    @total_work.setter
    def total_work(self, value):
        self.__total_work = value

    def is_available(self, cost_stamina):
        # Periksa apakah orang tersebut memiliki stamina yang cukup untuk melakukan suatu tugas
        return self.__stamina >= cost_stamina

    def pay_day(self):
        # Hitung total gaji berdasarkan total pekerjaan
        return self.__payment * self.__total_work

    def work(self, cost_stamina):
        # Mensimulasikan seseorang yang bekerja dengan mengurangi stamina dan meningkatkan total kerja
        self.__stamina -= cost_stamina
        self.__total_work += 1

    def __str__(self):
        # Representasi string dari instance Person
        class_name = self.__class__.__name__
        return f"{class_name} | {self.__name} | Total kerja: {self.__total_work} | Stamina: {self.__stamina} | Gaji: {self.pay_day()}"


class Manager(Person):
    def __init__(self, name, payment, stamina):
        # Konstruktor untuk Manager, mewarisi dari Person (Inheritance)
        super().__init__(name, payment, stamina)
        self.__list_worker = []

    @property
    def list_worker(self):
        # Getter untuk daftar pekerja yang dikelola oleh manajer
        return self.__list_worker

    def hire_worker(self, name):
        # Mempekerjakan pekerja baru, memastikan keunikan nama
        if name.lower() not in [worker.name.lower() for worker in self.__list_worker]:
            new_worker = Worker(name, 5000, 100)
            self.__list_worker.append(new_worker)
            self.work(10)  # reducing manager's stamina
            print(f"Berhasil mendapat pegawai baru")
        else:
            print("Sudah ada!")

    def fire_worker(self, name):
        # Memecat pekerja dengan menghapusnya dari daftar
        for worker in self.__list_worker:
            if worker.name == name:
                self.__list_worker.remove(worker)
                self.work(10)  # reducing manager's stamina
                print(f"Berhasil memecat {name}")
                return
        print("Nama tidak ditemukan")

    def give_work(self, name, bonus, cost_stamina):
        # Menugaskan pekerjaan kepada pekerja, meningkatkan bonus, dan mengurangi stamina
        for worker in self.__list_worker:
            if worker.name == name and worker.is_available(cost_stamina):
                worker.work(cost_stamina)
                worker.set_bonus(worker.get_bonus() + bonus)
                self.work(10)  # reducing manager's stamina
                print("Pegawai dapat menerima pekerjaan")
                print("========================================")
                print(f"Berhasil memberi pekerjaan kepada {name}")
                return
        print("Pegawai tidak ditemukan atau Stamina Pegawai Tidak Cukup!")


class Worker(Person):
    def __init__(self, name, payment, stamina):
        # Konstruktor untuk Pekerja, mewarisi dari Orang
        super().__init__(name, payment, stamina)
        self.__bonus = 0

    def work(self, cost_stamina):
        # Mensimulasikan pekerja yang bekerja, meningkatkan total pekerjaan, dan menghitung bonus
        super().work(cost_stamina)
        self.__bonus += 0  # no additional bonus for regular work

    def get_bonus(self):
        # Getter untuk bonus
        return self.__bonus

    def set_bonus(self, new_bonus):
        # Setter untuk bonus
        self.__bonus = new_bonus

    def pay_day(self):
        # Cek apakah total work == 0, jika ya maka gaji = 0
        if self.total_work == 0:
            return 0
        # Hitung total gaji berdasarkan total pekerjaan dan bonus
        return self.payment + self.__bonus


def main():
    name = input("Masukkan nama manajer: ")
    payment = int(input("Masukkan jumlah pembayaran: "))
    stamina = int(input("Masukkan stamina manajer: "))

    manager = Manager(name, payment, stamina)

    while manager.is_available(1):
        print(
            """
PACILOKA
-----------------------
1. Lihat status pegawai
2. Beri tugas
3. Cari pegawai baru
4. Pecat pegawai
5. Keluar
-----------------------
        """
        )
        action = int(input("Masukkan pilihan: "))

        if action == 1:
            for person in manager.list_worker[::-1] + [manager]:
                print(person)

        elif action == 3:
            name = input("Nama pegawai baru: ")
            manager.hire_worker(name)

        elif action == 2:
            name = input("Tugas akan diberikan kepada: ")
            bonus = int(input("Bonus pekerjaan: "))
            cost_stamina = int(input("Beban stamina: "))
            print("Hasil cek ketersediaan pegawai:")
            if any(
                worker.name == name and worker.is_available(cost_stamina)
                for worker in manager.list_worker
            ):
                manager.give_work(name, bonus, cost_stamina)
            else:
                print("Pegawai tidak dapat menerima pekerjaan. Stamina pegawai tidak cukup.")

        elif action == 4:
            name = input("Masukkan nama pegawai yang ingin dipecat: ")
            manager.fire_worker(name)

        elif action == 5:
            print(
                """
----------------------------------------
Berhenti mengawasi hotel, sampai jumpa !
----------------------------------------"""
            )
            return
    print(
        """
----------------------------------------
Stamina manajer sudah habis, sampai jumpa !
----------------------------------------"""
    )


if __name__ == "__main__":
    main()
