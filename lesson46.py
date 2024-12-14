import threading
import time


class Knight(threading.Thread):
    enemy_count = 100

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f"{self.name}, на нас напали!")
        days = 0
        while Knight.enemy_count > 0:
            time.sleep(1)
            days += 1
            Knight.enemy_count -= self.power
            if Knight.enemy_count < 0:
                Knight.enemy_count = 0
            day_word = "день" if days == 1 else "дня"
            print(f"{self.name}, сражается {days} {day_word}..., осталось {Knight.enemy_count} воинов.")

        print(f"{self.name} одержал победу спустя {days} {day_word}!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Все битвы закончились!")