import pyautogui
import random


def main():
    while True:
        # Рандомная пауза от 200 до 400 секунд
        pyautogui.PAUSE = random.randint(200, 400)

        # Сдвиг курсора по оси x в пикселях
        random_x = random.randint(-100, 100)

        # Сдвиг курсора по оси y в пикселях
        random_y = random.randint(-100, 100)

        # Рандомная скорость сдвига курсора от 0,25 до 1 секунды
        random_duration = random.uniform(0.25, 1)

        pyautogui.moveRel(random_x, random_y, duration=random_duration)


if __name__ == '__main__':
    main()
