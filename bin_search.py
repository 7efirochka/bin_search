
from random import randint


number_prog = randint(1, 101)
number_user = 101
print("Программа загадала число, угадай какое :)")
while number_user != number_prog:
    number_user = int(input())
    if number_user > number_prog:
        print("Бери меньше")
    elif number_user < number_prog:
        print("Возьми побольше")
    else:
        print(f"Верно, программа загадала число {number_prog}")

