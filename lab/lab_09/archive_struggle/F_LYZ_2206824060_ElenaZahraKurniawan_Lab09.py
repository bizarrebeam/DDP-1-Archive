# Import library random randint
from random import randint

# Membuat class untuk semua karakter yang ada di dalam game
class Entity:
    def __init__(self, name, hp, atk):
        self.__name = name
        self.__hp = hp
        self.__atk = atk

    def get_name(self):
        return self.__name

    def get_atk(self):
        return self.__atk

    def get_hp(self):
        return self.__hp

    def set_hp(self, new_hp):
        self.hp = new_hp

    def attack(self, other):
        other.take_damage(self.__atk)

    def take_damage(self, damage):
        self.__hp -= damage

    def is_alive(self):
        return self.__hp > 0

    def __str__(self):
        # Akan digunakan untuk print nama
        return self.__name

# Membuat class untuk pemain
class Player(Entity):
    def __init__(self, name, hp, atk, defense):
        super().__init__(name, hp, atk)
        self.__defense = defense

    def get_defense(self):
        return self.__defense

    def take_damage(self, damage):
        if isinstance(self, Boss):
           self.set_hp(self.get_hp() - damage)
        else:
            if self.__defense >= damage:
                damage = 0
            else:
                damage -= self.__defense
            self.set_hp(self.get_hp() - damage)

class Boss(Entity):
    def __init__(self, name, hp, atk):
        super().__init__(name, hp, atk)

    def attack(self, other):
        other.take_damage(self.get_atk())

# Membuat function program
def main():
    # Meminta ATK dan DEF Depram
    atk = int(input("Masukkan ATK Depram: "))
    defense = int(input("Masukkan DEF Depram: "))

    # Inisialisasi Depram dan musuh-musuh
    depram = Player("Depram", 100, atk, defense)
    enemies = [
        Entity(f"Enemy {i}", randint(20, 100), randint(10, 30))
        for i in range(randint(0, 1))
    ]
    enemies.append(Boss("Ohio Final Boss", randint(20, 100), randint(10, 30)))

    print(f"Terdapat {len(enemies)} yang menghadang Depram!")
    print("------------")

    for enemy in enemies:
        print(f"{enemy} muncul!")
        print()
        print("---Status---")
        print(f"{enemy.get_name():20} HP: {enemy.get_hp()}")
        print(f"{depram.get_name():20} HP: {depram.get_hp()}")
        print("------------")
        while enemy.is_alive() and depram.is_alive():
            print(f"{depram.get_name()} menyerang {enemy} dengan {depram.get_atk()}")
            enemy.take_damage(depram.get_atk())
            print(f"{enemy} menyerang {depram.get_name()} dengan {enemy.get_atk()} ATK!")
            
        if not depram.is_alive():
            print("------------")
            print()
            print("Tidak! Depram telah dikalahkan oleh musuhnya :(")
            return
        else:
            print(f"{enemy} telah kalah!")

        print("------------")
        print()

    print("Selamat! Semua musuh Depram telah kalah!")

# Memanggil function program
if __name__ == "__main__":
    main()