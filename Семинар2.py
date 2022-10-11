
# Задача 1. Напишите программу, которая принимает на
# вход цифру, обозначающую день недели, и выводит
# название этого дня недели.

from cmath import sqrt
import math

def Week():
    print("Введите день недели ")
    x = int(input())
    if x == 1:
        print("Понедельник")
    elif x == 2:
        print("Вторник")
    elif x == 3:
        print("Среда")
    elif x == 4:
        print("Четверг")
    elif x == 5:
        print("Пятница")
    elif x == 6:
        print("Суббота")
    elif x == 7:
        print("Воскресенье")
    else:
        print("Нет такого дня недели")            

# Задача 2. Напишите программу, которая принимает на
# вход координаты двух точек и находит расстояние между
# ними в 2D пространстве.
def Len():
    print("Введите координаты первой точки")
    point1 = [int(el) for el in input().split()]
    print("Введите координаты второй точки")
    point2 = [int(el) for el in input().split()]
    print("Расстояние = ", round(math.sqrt( (point1[0]-point2[0])**2 + (point1[1]-point2[1])**2 ), 2))

# Задача 3. Напишите программу, которая по заданному
# номеру четверти, показывает диапазон возможных
# координат точек в этой четверти (x и y).
def Quart():
    print("Введите номер четверти ")
    N = int(input())
    if N == 1:
        print ("X(0, +∞)   Y(0, +∞)")
    elif N == 2:
        print ("X(-∞, 0)   Y(0, +∞)")  
    elif N == 3:
        print ("X(-∞, 0)   Y(-∞, 0)")
    elif N == 4:
        print ("X(0, +∞)   Y(-∞, 0)")
    else:
        print ("Такой четверти нет")                         


# Задача 4. Напишите программу, которая на вход
# принимает число (N), а на выходе показывает все чётные
# числа от 1 до N.
def Chet():
    print("Введите N ")
    N= int(input())
    for i in range (2, N+1, 2):
        print(i, end = " ")
    print()

Week()
Len()
Quart()
Chet()
