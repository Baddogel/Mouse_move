import pyautogui
import random


def main():
    while True:
        pyautogui.PAUSE = random.randint(200, 400)
        random_x = random.randint(-100, 100)
        random_y = random.randint(-100, 100)
        random_duration = random.uniform(0.25, 1)
        pyautogui.moveRel(random_x, random_y, duration=random_duration)


if __name__ == '__main__':
    main()
