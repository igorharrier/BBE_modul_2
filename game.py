import random

class TreasureMap:
    def __init__(self, size=10):
        self.size = size
        self.treasure_x, self.treasure_y = self.generate_treasure_location()

    def generate_treasure_location(self):
        return random.randint(0, self.size - 1), random.randint(0, self.size - 1)

    def check_treasure(self, x, y):
        return self.treasure_x == x and self.treasure_y == y

    def get_hint(self, x, y):
        if abs(self.treasure_x - x) + abs(self.treasure_y - y) <= 3:
            return "Вы близко к сокровищу!"
        else:
            return "Сокровище еще далеко."

class Player:
    def __init__(self):
        self.attempts = 0

    def make_guess(self):
        try:
            coordinates = input("Введите координаты (формат: x, y): ")
            x, y = map(int, coordinates.split(','))
            self.attempts += 1
            return x, y
        except ValueError:
            print("Ошибка! Введите координаты в формате «x, y».")
            return None, None

class Game:
    def __init__(self):
        self.map = TreasureMap()
        self.player = Player()
        self.max_attempts = 20

    def start(self):
        print("Добро пожаловать в игру «Поиск сокровища»!")
        while self.player.attempts < self.max_attempts:
            x, y = self.player.make_guess()
            if x is None or y is None:
                continue
            if self.map.check_treasure(x, y):
                print("Поздравляем! Вы нашли сокровище.")
                break
            else:
                print(self.map.get_hint(x, y))
            print(f"Попыток: {self.player.attempts}")
        if self.player.attempts >= self.max_attempts:
            print("Количество попыток исчерпано. Сокровище не найдено.")

if __name__ == "__main__":
    game = Game()
    game.start()
