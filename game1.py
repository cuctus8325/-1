import time
import random

hp = 100
speed = 0
boost = 1
distance = 400

while True:
    print("Игра идет")
    if distance <= 0:
        print("\nУРА! ПОБИДА!")
        break

    rand = random.randint(1, 10)
    if rand == 1:
        print("На пути дерево, что вы будете делать ")
        choice = input("1. Повернуть вправо\n2.Повернуть влево\n3.Прыгнуть\nВведите номер: ")
        trueChoice = random.randint(1,3)
        print(trueChoice)
        if choice == trueChoice:
            print("Вы избежали дерево")
        else:
        print("Вы столкнулись с деревом")
        hp = hp - 5
        speed = speed // 2
    elif rand == 2:
        print("Вы столкнулись с Йети")
        hp = hp - 7
        speed = speed // 2
    elif rand == 3:
        print("Вы столкнулись с камнем")
        hp = hp - 3
        speed = speed // 2

    distance = distance - speed
    speed = speed + boost
    print(f"\nУ вас осталось {hp} хп")
    print(f'\nОсталось проехать {distance} метров')
    print(f"Ваша скорость: {speed} м/с")
    time.sleep(1)