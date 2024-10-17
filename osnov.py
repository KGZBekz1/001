#основной код
import random
from decouple import config

# Читаем параметры из файла
RANGE_START = config('RANGE_START', cast=int)
RANGE_END = config('RANGE_END', cast=int)
ATTEMPTS = config('ATTEMPTS', cast=int)
INITIAL_CAPITAL = config('INITIAL_CAPITAL', cast=int)

def play_game():
    capital = INITIAL_CAPITAL
    number_to_guess = random.randint(RANGE_START, RANGE_END)
    attempts_left = ATTEMPTS

    print(f"Добро пожаловать в игру 'Угадай число'!")
    print(f"Вы должны угадать число от {RANGE_START} до {RANGE_END}.")
    print(f"У вас {ATTEMPTS} попыток и {capital} единиц капитала.")

    while attempts_left > 0 and capital > 0:
        try:
            # Запрашиваем ставку
            bet = int(input(f"\nВведите вашу ставку (оставшийся капитал: {capital}): "))
            if bet > capital:
                print("Вы не можете ставить больше, чем у вас есть.")
                continue

            # Запрашиваем число, которое игрок пытается угадать
            guess = int(input(f"Попробуйте угадать число (осталось попыток: {attempts_left}): "))

            # Проверяем, угадал ли игрок
            if guess == number_to_guess:
                capital += bet
                print(f"Поздравляю! Вы угадали число. Ваш текущий капитал: {capital}.")
                break
            else:
                capital -= bet
                attempts_left -= 1
                print(f"Неверно. Ваш текущий капитал: {capital}. Осталось попыток: {attempts_left}.")
        except ValueError:
            print("Пожалуйста, введите корректное число.")

    # Проверяем результаты игры
    if capital <= 0:
        print("К сожалению, вы проиграли весь капитал.")
    elif attempts_left == 0:
        print(f"У вас закончились попытки. Загаданное число было {number_to_guess}.")
    else:
        print("Вы выиграли!")

if __name__ == "__main__":
    play_game()
